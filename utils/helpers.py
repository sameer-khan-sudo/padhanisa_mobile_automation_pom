import random
import subprocess

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Get the Android version
def get_android_version():
    try:
        # Run the adb shell command to get the Android version
        version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"])
        # Decode the byte output to string and strip any extraneous whitespace
        android_version = version.decode("utf-8").strip()
        print(f"Detected Android version: {android_version}")  # Print the Android version
        return android_version
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to get Android version. Ensure ADB is installed and the device is connected.")

# Generate random mobile number
def generate_random_mobile_number():
    return "9" + ''.join([str(random.randint(0, 9)) for _ in range(9)])


# Scroll down the page using Appium's UiScrollable class
def scroll_down(driver):
    driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )

# Tap on the screen
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


# Verify actual text on the screen with the expected text
def verify_text_on_screen(driver, locators, expected_texts):
    # Ensure locators and expected_texts are lists
    if not isinstance(locators, list):
        locators = [locators]
    if not isinstance(expected_texts, list):
        expected_texts = [expected_texts]

    try:
        for locator, expected_text in zip(locators, expected_texts):
            # Wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(locator)
            )

            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(locator)
            )

            # Assert that the element is visible
            assert element.is_displayed(), f"Element located by {locator} is not visible on the screen."

            # Get the text from 'content-desc' attribute
            actual_text = element.get_attribute('content-desc')

            # Verify if the actual text matches the expected text
            assert actual_text == expected_text, f"Text does not match! Expected: {expected_text}, Got: {actual_text}"

            print(
                f"\nText verification passed.\n-------------------------\nActual Text : '{actual_text}'\nExpected Text : '{expected_text}'.\n")

    except TimeoutException as e:
        print(f"Timeout: Failed to find element with locator: {locator}")
        driver.save_screenshot("timeout_error.png")
        raise

    except NoSuchElementException as e:
        print(f"Error: Element with locator {locator} was not found.")
        driver.save_screenshot("no_element_error.png")
        raise

    except AssertionError as e:
        print(f"Assertion failed: {str(e)}")
        driver.save_screenshot("assertion_error.png")
        raise

    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {str(e)}")
        driver.save_screenshot("unexpected_error.png")
        raise