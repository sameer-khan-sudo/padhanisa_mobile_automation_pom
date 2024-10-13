import random
from time import time
from datetime import datetime, timedelta

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Utility function to wait for an element to be clickable and then click it
def wait_and_click(self, by, value):
    try:
        # Locate the element directly without waiting
        element = self.driver.find_element(by, value)

        # Check if the element is displayed and clickable
        if element.is_displayed() and element.is_enabled():
            element.click()
            # print("Successfully clicked the element.")
        else:
            raise Exception("Element is not displayed or not clickable")
    except Exception as e:
        # Handle the exception as needed
        print(f"Failed to click element: {str(e)}")
        raise



# Generate and return a random 10-digit mobile number
def generate_random_mobile_number():
    mobile_number = "9" + ''.join([str(random.randint(0, 9)) for _ in range(9)])  # Starts with '9' for a valid number
    return mobile_number

# Tap on the screen to close keyboard
def tap_at_coordinates(self):
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(562, 544)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

# Perform scroll down
def scroll_down(self):
    self.driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )

# Returns the trial expiry date in a formatted string.
def get_formatted_expiry_date(days=14):
    current_date = datetime.now()
    expiry_date = current_date + timedelta(days=days)
    return expiry_date.strftime("%d %B %Y")

# Close the keyboard
def hide_keyboard(self):
    self.driver.hide_keyboard()


# Clicks the 'Start Learning' button
def click_start_learning(self):
    start_learning_button = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Start Learning"]')
    wait_and_click(self, *start_learning_button)
