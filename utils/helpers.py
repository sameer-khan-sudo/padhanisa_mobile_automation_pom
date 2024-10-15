import random
from appium.webdriver.common.appiumby import AppiumBy

def generate_random_mobile_number():
    return "9" + ''.join([str(random.randint(0, 9)) for _ in range(9)])

def scroll_down(driver):
    driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )