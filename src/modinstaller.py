import os, configparser, subprocess
from distutils.dir_util import copy_tree
from sys import platform


config = configparser.ConfigParser()
config.read("settings.ini")

userdataModsDirectory = os.path.normpath(config['DIRECTORY']['userdatamods'])
sevenZipinstallation = os.path.normpath(config["DIRECTORY"]["7-zipInstallation"])

def install(link):

    if platform == "linux":
        if link.lower().endswith('zip') or link.lower().endswith('rar') or link.lower().endswith("7z"):
            subprocess.Popen(["7z", "x", link, f"-o{userdataModsDirectory}", "-y"])
            return True
        if os.path.isdir(link):
            _, b = os.path.split(link)
            copy_tree(link, os.path.join(userdataModsDirectory, b))
            return True

    elif platform == "win32":
        if link.lower().endswith('zip') or link.lower().endswith('rar') or link.lower().endswith("7z"):
            subprocess.Popen(f'"{ os.path.join(sevenZipinstallation, "7z.exe") }" x {link} -o"{userdataModsDirectory}" -y')
            return True
        if os.path.isdir(link):
            # copy subdirectory example
            _, b = os.path.split(link)
            copy_tree(link, os.path.join(userdataModsDirectory, b))
            return True
