import random

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def generate_random_mobile_number():
    return "9" + ''.join([str(random.randint(0, 9)) for _ in range(9)])

def scroll_down(driver):
    driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )


def tap_on_screen(driver):
    try:
        actions = ActionChains(driver)

        # Create a new ActionBuilder with a touch pointer input
        touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        actions.w3c_actions = ActionBuilder(driver, mouse=touch_input)

        # Move to the specified location and perform the tap action
        actions.w3c_actions.pointer_action.move_to_location(82, 348)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    except Exception as e:
        # Handle any errors that occur during the tap action
        print(f"An error occurred while performing tap action: {e}")
        pytest.fail(f"Tap action failed due to: {e}")

