import pytest
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.fixture(scope="module")
def driver():
    caps = {
        "platformName": "Android",
        "platformVersion": "14.0",
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
    # driver.implicitly_wait(120)
    yield driver
    # driver.quit()  # Uncomment this line if you want to quit the driver after the tests
