from appium import webdriver
import warnings


class Driver:

    def __init__(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Android Emulator",
            "appium:chromedriverExecutable": '/usr/bin/chromedriver',
            "appPackage": 'com.android.chrome',
            "appActivity": 'com.google.android.apps.chrome.Main'
        }
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self.instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
