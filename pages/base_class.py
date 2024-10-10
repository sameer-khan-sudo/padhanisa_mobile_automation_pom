import logging

from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)  # Initialize a logger for the class
        logging.basicConfig(level=logging.INFO)  # Set logging level (you can configure this as needed)

    def enter_text(self, locator, text):
        # Use wait_and_click to ensure the element is clickable before sending keys
        by, value = locator  # Unpack locator tuple
        self.wait_and_click(by, value)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(text)

    def verify_text_on_screen(self, locator, expected_text):
        # Wait for the element and verify its text
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        # Get the content description attribute
        actual_text = element.get_attribute('content-desc')

        # Assert that the actual text matches the expected text
        assert actual_text == expected_text, f"Expected text '{expected_text}' not found, got '{actual_text}'"

    # Utility function to wait for an element to be clickable and then click it
    def wait_and_click(self, by, value, timeout=20):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((by, value)))
            element = wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except TimeoutException:
            print(f"Timeout occurred while waiting for element: {value}")
            self.driver.save_screenshot(f"{value}_timeout.png")
            raise
        except NoSuchElementException:
            print(f"Element not found: {value}")
            self.driver.save_screenshot(f"{value}_not_found.png")
            raise
        except Exception as e:
            print(f"An error occurred while clicking the element: {str(e)}")
            self.driver.save_screenshot(f"{value}_click_error.png")
            raise
