import random
from datetime import datetime, timedelta

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementNotVisibleException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

# Generate and return a random 10-digit mobile number
def generate_random_mobile_number():
    mobile_number = "9" + ''.join([str(random.randint(0, 9)) for _ in range(9)])  # Starts with '9' for a valid number
    return mobile_number

# Tap on the screen to close keyboard
def tap_at_coordinates(self):
    """Reusable method to tap at specific coordinates."""
    try:
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(562, 544)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    except Exception as e:
        pytest.fail(f"Failed to tap on the screen: {str(e)}")

# Perform scroll down
def scroll_down(self):
    """Scrolls forward in a scrollable view."""
    try:
        self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR,
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )
    except Exception as e:
        pytest.fail(f"Failed to scroll down: {str(e)}")


# Returns the trial expiry date in a formatted string.
def get_formatted_expiry_date(days=14):
    current_date = datetime.now()
    expiry_date = current_date + timedelta(days=days)
    return expiry_date.strftime("%d %B %Y")

# Close the keyboard
def hide_keyboard(self):
    try:
        self.driver.hide_keyboard()
    except Exception as e:
        print(f"Failed to hide keyboard: {str(e)}")
        # Alternative method to hide keyboard
        try:
            done_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Done']"))
            )
            done_button.click()
        except TimeoutException:
            print("Could not find 'Done' button to hide keyboard")

# Clicks the 'Start Learning' button
def click_start_learning(self):
    try:
        start_learning_button = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Start Learning"]')
        # Pass 'self' explicitly along with the locator tuple
        wait_and_click(self, *start_learning_button)
    except (
            NoSuchElementException,
            TimeoutException,
            StaleElementReferenceException,
            ElementNotVisibleException,
            WebDriverException) as e:
        print(f"Error while clicking on Start Learning button: {str(e)}")

