import pytest
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="session")
def user_data():
    """Fixture to load test data from JSON file."""
    with open('test_data.json') as f:
        data = json.load(f)
    return data


@pytest.fixture(scope="class")
def driver(request):
    """Fixture to setup Appium driver."""
    caps = {
        "platformName": "Android",
        "platformVersion": "15.0",
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
    driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(caps))
    driver.implicitly_wait(120)
    request.cls.driver = driver
    yield driver
    # driver.quit()
