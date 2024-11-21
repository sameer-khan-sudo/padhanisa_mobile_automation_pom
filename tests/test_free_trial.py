import logging
from logging import raiseExceptions

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver
from pages.create_profile_page import CreateProfile
from pages.login_page import LoginPage
from pages.plan_page import PlanPage
from pages.profile_page import ProfilePage
from utils.helpers import scroll_down, verify_text_on_screen

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define user type
USER_TYPE = 'NEW'

@pytest.mark.usefixtures("driver")
class TestFreeTrial:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for initializing driver and page objects."""
        self.driver = driver
        self.login = LoginPage(driver)
        self.create_user_profile = CreateProfile(driver)
        self.plan = PlanPage(driver)
        self.profile = ProfilePage(driver)
        self.wait = WebDriverWait(driver, 10)

    # Test for existing user login
    @pytest.mark.skipif(USER_TYPE != 'EXIST', reason="Skipped because USER_TYPE is not 'EXIST'")
    def test_perform_exist_user_login(self):
        """Login with an existing user and select a profile."""
        try:
            logging.info("Attempting login with an existing user.")
            self.login.exist_user_login('9412856057')
            logging.info("Login with existing user successful.")

            # Select profile
            self.profile.select_profile('Jack')
            logging.info("Profile selection successful.")

        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    # Test for new user login and profile creation
    @pytest.mark.skipif(USER_TYPE != 'NEW', reason="Skipped because USER_TYPE is not 'NEW'")
    def test_login_and_create_user_profile(self):
        """Login as a new user and create a user profile."""
        try:
            logging.info("Starting login process...")
            self.login.click_sign_in()
            self.login.perform_login()
            logging.info("Login successful.")

            # Create User Profile
            self.create_user_profile.enter_first_name('Jack')
            logging.info("Entered first name.")
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
            pytest.fail(f"Test failed: {e}")

    # Test for activating free trial plan
    def test_activate_free_trial_plan(self):
        """Activate the free trial plan and verify success."""
        try:

            self.plan.wait_and_click(AppiumBy.ACCESSIBILITY_ID, "Free Trial")
            logging.info("Clicked on the Free Trial button.")
            locators = [
                self.plan.GO_PREMIUM_HEADER_LOCATOR,
                self.plan.FREE_TRIAL_BENEFITS_LOCATOR,
            ]
            expected_texts = [
                self.plan.EXPECTED_GO_PREMIUM_HEADER_TEXT,
                self.plan.EXPECTED_FREE_TRIAL_BENEFITS_TEXT,
            ]


            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.FREE_TRIAL_FIELD_LOCATOR)

            verify_text_on_screen(self.driver, locators, expected_texts)
            logging.info("Verified texts on the screen successfully.")

            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.CONTINUE_BUTTON_LOCATOR)

            locators = [
                self.plan.FREE_TRIAL_ACTIVATED_HEADER_LOCATOR,
                self.plan.YOUR_TEXT_LOCATOR,
                self.plan.DAYS_FREE_PREMIUM_LOCATOR,
                self.plan.IS_NOW_ACTIVE_LOCATOR,
                self.plan.TRIAL_EXPIRY_MESSAGE_LOCATOR
            ]
            expected_texts = [
                self.plan.EXPECTED_FREE_TRIAL_TEXT,
                self.plan.EXPECTED_YOUR_TEXT,
                self.plan.EXPECTED_DAYS_FREE_PREMIUM_TEXT,
                self.plan.EXPECTED_IS_NOW_ACTIVE_TEXT,
                self.plan.EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT
            ]
            verify_text_on_screen(self.driver, locators, expected_texts)
            logging.info("Successfully verified trial activation details.")
        except Exception as e:
            logging.error(f"Error while activating free trial plan: {e}")
            pytest.fail(f"Failed to activate free trial plan: {e}")

    # Test for clicking on Start Learning and verifying the Premium tag
    def test_click_start_learning(self):
        """Click on 'Start Learning' button and verify 'Premium' tag."""
        try:
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.START_LEARNING_BUTTON_LOCATOR)
            logging.info("Clicked on the 'Start Learning' button.")

            premium_tag_locator = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Premium"]')
            if premium_tag_locator.is_displayed():
                logging.info("Trial Activated Successfully!")
        except Exception as e:
            logging.error(f"Error while clicking on 'Start Learning' button: {e}")
            pytest.fail(f"Failed to click on 'Start Learning' button: {e}")
