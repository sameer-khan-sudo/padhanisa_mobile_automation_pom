import random

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# Generate and return a random 10-digit mobile number
def generate_random_mobile_number(self):
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
        pass
        # pytest.fail(f"Failed to tap at coordinates ({x}, {y}): {str(e)}")


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
