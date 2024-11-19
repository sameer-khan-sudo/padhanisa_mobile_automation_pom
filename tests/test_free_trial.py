import logging
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

# Importing required classes and utilities
from pages.base_class import BaseClass
from pages.create_profile_page import CreateProfile
from pages.login_page import LoginPage
from pages.plan_page import PlanPage
from pages.profile_page import ProfilePage
from utils.helpers import scroll_down, verify_text_on_screen

# Configure logging
logging.basicConfig(level=logging.INFO)


@pytest.mark.usefixtures("driver")
class TestFreeTrial:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # Setup for initializing driver and page objects
        self.driver = driver
        self.login = LoginPage(driver)
        self.create_user_profile = CreateProfile(driver)
        self.plan = PlanPage(driver)
        self.profile = ProfilePage(driver)
        self.wait = WebDriverWait(driver, 10)

    # Perform login with new user
    @pytest.mark.skip
    @pytest.mark.dependency(name="LOGIN")
    def test_perform_login(self):
        try:
            self.login.click_sign_in()
            self.login.perform_login()
            logging.info("Login successful.")
        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    # perform login with an existing user
    @pytest.mark.dependency(name="LOGIN")
    def test_perform_exist_user_login(self):
        try:
            self.login.exist_user_login('9412856057')
            logging.info("Login with existing user successful.")

            # Select profile
            self.profile.select_profile('Jack')
        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    # Create a new user profile
    @pytest.mark.skip
    def test_create_user_profile(self):
        try:
            logging.info("Starting profile creation...")

            self.create_user_profile.enter_first_name('Jack')
            logging.info("Entered first name.")

            self.create_user_profile.enter_last_name('Doe')
            logging.info("Entered last name.")

            self.create_user_profile.select_voice_type('Male')
            logging.info("Voice type selected.")

            scroll_down(self.driver)
            logging.info("Scrolled down the page.")

            self.create_user_profile.select_age('16 - 25')
            logging.info("Age selected.")

            self.create_user_profile.select_skill_level('I Am A Singer')
            logging.info("Skill level selected.")

            self.create_user_profile.click_continue_button()
            logging.info("Clicked on Continue button.")
        except Exception as e:
            pytest.fail(f"Profile creation failed: {e}")

    # Activate free trial plan
    def test_activate_free_trial_plan(self):
        try:
            # Click on the Free Trial button
            self.plan.wait_and_click(AppiumBy.ACCESSIBILITY_ID, "Free Trial")
            logging.info("Clicked on the Free Trial button.")

            # Locators and expected text to verify
            locators = [
                self.plan.GO_PREMIUM_HEADER_LOCATOR,
                self.plan.FREE_TRIAL_BENEFITS_LOCATOR,
                # self.plan.TRIAL_EXPIRY_MESSAGE_LOCATOR
            ]
            expected_texts = [
                self.plan.EXPECTED_GO_PREMIUM_HEADER_TEXT,
                self.plan.EXPECTED_FREE_TRIAL_BENEFITS_TEXT,
                #                 self.plan.EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT,
            ]

            # Verify the text on the screen
            verify_text_on_screen(self.driver, locators, expected_texts)
            logging.info("Verified the actual and expected text on the screen successfully.")

            # Click on Free Trial field
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.FREE_TRIAL_FIELD_LOCATOR)

            # Click on 'Continue' button
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.CONTINUE_BUTTON_LOCATOR)

            # Locators and expected text to verify
            locators = [
                self.plan.TRIAL_EXPIRY_MESSAGE_LOCATOR
            ]
            expected_texts = [
                self.plan.EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT
            ]

            # Verify the success message and plan/trial expiry message
            verify_text_on_screen(self.driver, locators, expected_texts)
            logging.info("Verified the actual and expected text on the screen successfully.")


        except Exception as e:
            # Handle failures and provide meaningful messages
            logging.error(f"Error while activating free trial plan: {e}")
            pytest.fail(f"Failed to activate free trial plan: {e}")
