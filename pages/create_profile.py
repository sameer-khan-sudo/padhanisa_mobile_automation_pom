import time
from datetime import timedelta

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass


class CreateProfile(BaseClass):
    # Locators for elements
    FIRST_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
    LAST_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    VOICE_TYPE = (AppiumBy.XPATH, "//android.view.View[@content-desc='Male']")
    AGE_DROPDOWN = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Select']")
    SKILL_LEVEL = (AppiumBy.XPATH, "//android.view.View[@content-desc='Never Learnt Before']")
    EMAIL_ID = (AppiumBy.XPATH, "//android.widget.EditText")
    CONTINUE_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Continue"]')

    # Enter first name
    def enter_first_name_field(self, first_name):
        try:
            self.wait_and_click(*self.FIRST_NAME_FIELD)
            self.enter_text(self.FIRST_NAME_FIELD, str(first_name))
            time.sleep(0.5)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error entering first name: {e}")  # Log the error

    # Enter last name
    def enter_last_name_field(self, last_name):
        try:
            self.wait_and_click(*self.LAST_NAME_FIELD)
            self.enter_text(self.LAST_NAME_FIELD, str(last_name))
            time.sleep(0.5)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error entering last name: {e}")  # Log the error

    # Select voice type
    def select_voice_type(self):
        try:
            self.wait_and_click(*self.VOICE_TYPE)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error selecting voice type: {e}")  # Log the error

    # Select age from dropdown
    def select_age(self, age):
        try:
            self.wait_and_click(*self.AGE_DROPDOWN)
            age_value_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{age}")')
            self.wait_and_click(*age_value_locator)
            time.sleep(0.5)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error selecting age: {e}")  # Log the error

    # Select skill level
    def select_skill_level(self, skill_value):
        try:
            skill_value_locator = (AppiumBy.XPATH, f"//android.view.View[@content-desc='{skill_value}']")
            self.wait_and_click(*skill_value_locator)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error selecting skill level: {e}")  # Log the error

    # Enter email ID
    def enter_email_id(self, email):
        try:
            self.wait_and_click(*self.EMAIL_ID)
            self.enter_text(self.EMAIL_ID, str(email))
            time.sleep(0.5)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error entering email ID: {e}")  # Log the error

    # Click continue button
    def click_on_continue_button(self):
        try:
            self.wait_and_click(*self.CONTINUE_BUTTON)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error clicking continue button: {e}")  # Log the error
