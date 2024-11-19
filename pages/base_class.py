from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    # Locator for reuse
    LOCATOR_SKIP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Skip")
    LOCATOR_SINGING_CLASSES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Singing Classes")')

    # Click on 'Skip' button
    def click_skip(self):
        self.wait_and_click(*self.LOCATOR_SKIP_BUTTON)


    # Wait for element and click on it
    def wait_and_click(self, by, value, timeout=20):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except Exception as e:
            print(f"Error clicking element ({by}, {value}): {e}")
            raise

    # Enter the data in fields
    def enter_text(self, locator, text, timeout=20):
        by, value = locator
        try:
            self.wait_and_click(by, value, timeout)
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            # element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error entering text in field ({by}, {value}): {e}")
            raise

    # Close the Keyboard
    def close_keyboard(self):
        self.driver.hide_keyboard()

    # Click 'Singing Classes' tab
    def select_class_module(self):
        self.wait_and_click(*self.LOCATOR_SINGING_CLASSES)

