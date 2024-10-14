from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    # Enter text into an input field
    def enter_text(self, locator, text):
        by, value = locator  # Unpack locator tuple
        self.wait_and_click(by, value)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(text)

    # Verify if the displayed text matches the expected text
    def verify_text_on_screen(self, locators, expected_texts):
        if not isinstance(locators, list):
            locators = [locators]
        if not isinstance(expected_texts, list):
            expected_texts = [expected_texts]

        for locator, expected_text in zip(locators, expected_texts):
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            assert element.is_displayed(), f"Element {locator} not visible."
            actual_text = element.get_attribute('content-desc')
            assert expected_text in actual_text, f"Expected: {expected_text}, Got: {actual_text}"

    # Wait and perform click on the button/fields/tab
    def wait_and_click(self, by, value, timeout=10):
        try:
            # Wait for the element to be clickable
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((by, value)))
            # Click the element
            element.click()
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with locator ({by}, {value}) was not found in the DOM")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element with locator ({by}, {value}) was not interactable")


