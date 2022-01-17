import os
import sys
import requests
import zipfile
import shutil
from xml.etree import ElementTree
from enum import Enum

from utils import constains
from utils.constains import *
from utils.process_utils import shell


class OSType(Enum):
    LINUX = 'linux'
    MAC = 'mac'
    WIN = 'win'


class BrowserType(Enum):
    CHROME = 'google-chrome'
    CHROMIUM = 'chromium'


class ChromeUtile:
    def __init__(self):
        platform = sys.platform
        self.os_name = OSType.LINUX if platform.startswith("'linux'") else OSType.MAC if platform.startswith(
            "darwin") else OSType.WIN

    def get_version(self):
        cmd_map = {
            BrowserType.CHROME:{
                OSType.LINUX: 'google-chrome --version || google-chrome-stable --version',
                OSType.MAC: r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version',
                OSType.WIN: r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'
            },
            BrowserType.CHROMIUM: {
                OSType.LINUX: 'chromium --version || chromium-browser --version',
                OSType.MAC: r'/Applications/Chromium.app/Contents/MacOS/Chromium --version',
                OSType.WIN: r'reg query "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Google Chrome" /v version'
            }
        }

        cmd = cmd_map[BrowserType.CHROME][self.os_name]
        stdout = shell(cmd)
        try:
            return VERSION_RE.findall(stdout)[0]
        except IndexError:
            cmd = cmd_map[BrowserType.CHROMIUM][self.os_name]
            stdout = shell(cmd)
            try:
                return VERSION_RE.findall(stdout)[0]
            except IndexError:
                print(
                    f"Couldn't get browser version")
                sys.exit(-1)

    def get_ostype(self):
        os_type = self.os_name.value
        return os_type

    def get_chrome_data_path(self):
        return self.chrome_data_path

    def copy_chrome_data(self):
        data_path_map = {
            BrowserType.CHROME: {
                OSType.MAC: r'Library/Application Support/Google/Chrome',
                OSType.WIN: r'AppData\Local\Google\Chrome\User Data'
            }
        }
        chrome_data_path = os.path.join(os.path.expanduser("~"), data_path_map[BrowserType.CHROME][self.os_name])
        self.chrome_data_path = f"{chrome_data_path} ams"
        if not os.path.exists(self.chrome_data_path):
            try:
                shutil.copytree(chrome_data_path, self.chrome_data_path, symlinks=True, dirs_exist_ok=True)
            except:
                pass



class ChromeDriver:
    def __init__(self):
        self.driver_path = os.path.dirname(DRIVER_PATH)
        self.driver_file = DRIVER_PATH
        self.driver_url = "https://chromedriver.storage.googleapis.com"

        self.chrome = ChromeUtile()
        self.os_type = self.chrome.get_ostype()

    def get_version(self):
        try:
            os.chmod(self.driver_path, 0o755)
        except Exception:
            pass

        cmd = f'{self.driver_file} --version'
        stdout = shell(cmd)
        try:
            return VERSION_RE.findall(stdout.split()[1])[0]
        except IndexError:
            return 0

    def get_chromedriver(self, version):
        match_list = []
        if "win" in self.os_type:
            ot = "win32"
        else:
            os_architecture = 64 if sys.maxsize > 2**32 else 32
            ot = f"{self.os_type}{os_architecture}"
        res = requests.get(self.driver_url, timeout=30).text
        xmlns = "{http://doc.s3.amazonaws.com/2006-03-01}"
        root = ElementTree.fromstring(res)
        for child in  root.findall(f"{xmlns}Contents"):
            key = child.find(f"{xmlns}Key").text
            if version in key and "chromedriver" in key:
                if ot in key:
                    match_list.append(key)

        url = f"{self.driver_url}/{match_list[-1]}"
        self.driver_zip = os.path.join(self.driver_path, os.path.basename(url))
        res = requests.get(url)

        with open(self.driver_zip, "wb") as file:
            file.write(res.content)

    def unzip_file(self):
        if zipfile.is_zipfile(self.driver_zip):
            fz = zipfile.ZipFile(self.driver_zip)
            for file in fz.namelist():
                fz.extract(file, self.driver_path)


    def check_version(self):
        chrome_version = self.chrome.get_version()
        if self.get_version() != chrome_version:
            self.get_chromedriver(chrome_version)
            self.unzip_file()

def init_chrome():
    chrome_driver = ChromeDriver()
    chrome_driver.check_version()
    chrome_util = ChromeUtile()
    chrome_util.copy_chrome_data()
    constains.CHROME_DATA_PATH = chrome_util.get_chrome_data_path()
