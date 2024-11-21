from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

from conftest import driver
from pages.base_class import BaseClass
from utils.helpers import tap_on_screen

# Set up logging for better debugging information
logging.basicConfig(level=logging.INFO)

class CreateProfile(BaseClass):
    FIRST_NAME_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
    LAST_NAME_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
    AGE_DROPDOWN_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Select")')
    EMAIL_ID_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    CONTINUE_BUTTON = (AppiumBy.XPATH,'//android.widget.Button[@content-desc="Continue"]')

    def enter_first_name(self, first_name):
        try:
            self.wait_and_click(*self.FIRST_NAME_FIELD)
            self.enter_text(self.FIRST_NAME_FIELD, first_name)
            self.close_keyboard()
            logging.info("First name entered successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error entering first name: {e}")

    def enter_last_name(self, last_name):
        try:
            self.wait_and_click(*self.LAST_NAME_FIELD)
            self.enter_text(self.LAST_NAME_FIELD, last_name)
            self.close_keyboard()
            logging.info("Last name entered successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error entering last name: {e}")

    def select_voice_type(self, voice_type):
        VOICE_TYPE_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{voice_type}")')
        try:
            self.wait_and_click(*VOICE_TYPE_LOCATOR)
            logging.info(f"Voice type '{voice_type}' selected successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error selecting voice type '{voice_type}': {e}")

    def select_age(self, age_value):
        AGE_VALUE = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{age_value}")')
        try:
            self.wait_and_click(*self.AGE_DROPDOWN_LOCATOR)
            logging.info("Age dropdown opened successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error opening age dropdown: {e}")
            return

        try:
            self.wait_and_click(*AGE_VALUE)
            logging.info(f"Age '{age_value}' selected successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error selecting age '{age_value}': {e}")

    def select_skill_level(self, skill_level):
        SKILL_LEVEL_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{skill_level}")')
        try:
            self.wait_and_click(*SKILL_LEVEL_LOCATOR)
            logging.info(f"Skill level '{skill_level}' selected successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error selecting skill level '{skill_level}': {e}")


    def enter_email_id(self, email_id):
        try:
            self.wait_and_click(*self.EMAIL_ID_FIELD)
            self.enter_text(self.EMAIL_ID_FIELD, email_id)
            self.close_keyboard()
            logging.info("Email entered successfully.")
            self.close_keyboard()
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error entering email id: {e}")

    def click_continue_button(self):
        try:
            self.wait_and_click(*self.CONTINUE_BUTTON)
            logging.info("Continue button clicked successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error clicking continue button: {e}")