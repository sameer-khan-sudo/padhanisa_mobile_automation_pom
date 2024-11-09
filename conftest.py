import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from utils.helpers import get_android_version


@pytest.fixture(scope="module")
def driver():
    android_version = get_android_version()  # Get the dynamic Android OS version

    caps = {
        "platformName": "Android",
        "platformVersion": android_version,  # Set the dynamic version here
        "deviceName": "Pixel",
        "appPackage": "com.saregama.edutech.uat",
        "appActivity": "com.saregama.edutech.MainActivity",
        "automationName": "UiAutomator2",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 6000,
        "appium:connectHardwareKeyboard": True,
        "appium:autoGrantPermissions": True,
        "appium:skipUnlock": True,
        "appium:unicodeKeyboard": False,
        "appium:resetKeyboard": True,
        "appium:ignoreUnimportantViews": True,
        "appium:enablePerformanceLogging": True,
        "appium:adbExecTimeout": 90000,
        "appium:uiautomator2ServerInstallTimeout": 120000,
        "showTaps": True,
        "noReset": False,
        "fullReset": False,
        "appium:disableIdLocatorAutocompletion": True
    }

    url = 'http://localhost:4723'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps))
    yield driver
    # driver.quit()  # Uncomment this line if you want to quit the driver after the tests
