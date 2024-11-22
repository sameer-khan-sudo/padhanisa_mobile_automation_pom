import logging  # For logging test execution details.
import time
from pydoc import plain

import pytest  # For writing and managing tests.
from appium.webdriver.common.appiumby import AppiumBy  # Appium-specific locators.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver  # Shared driver setup.
from pages.create_profile_page import CreateProfile  # Page object for "Create Profile".
from pages.login_page import LoginPage  # Page object for "Login".
from pages.plan_page import PlanPage  # Page object for "Plan".
from pages.profile_page import ProfilePage  # Page object for "Profile".
from pages.razor_pay_page import RazorPayPage
from utils.helpers import verify_text_on_screen  # Helper functions for scrolling and text verification.

# Configure logging
logging.basicConfig(level=logging.INFO)

# Test Data
USER_TYPE = 'EXIST'
EXISTING_USER_PHONE = '1100000000'
PROFILE_NAME = 'Jack'

NEW_USER_FIRST_NAME = 'Jack'
NEW_USER_VOICE_TYPE = 'Male'
NEW_USER_AGE_GROUP = '16 - 25'
NEW_USER_SKILL_LEVEL = 'I Am A Singer'
UPI_ID = 'success@razorpay'



@pytest.mark.usefixtures("driver")
class TestFreeTrial:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Initialize driver and page objects."""
        self.driver = driver
        self.login = LoginPage(driver)
        self.create_user_profile = CreateProfile(driver)
        self.plan = PlanPage(driver)
        self.profile = ProfilePage(driver)
        self.razorpay = RazorPayPage(driver)
        self.wait = WebDriverWait(driver, 10)

    # Login with an existing user
    @pytest.mark.skipif(USER_TYPE != 'EXIST', reason="Skipped because USER_TYPE is not 'EXIST'")
    def test_perform_exist_user_login(self):
        """Login with an existing user and select a profile."""
        try:
            logging.info("Attempting login with an existing user.")
            self.login.exist_user_login(EXISTING_USER_PHONE)
            logging.info("Login with existing user successful.")

            # Select profile
            self.profile.select_profile(PROFILE_NAME)
            logging.info("Profile selection successful.")
            time.sleep(1)

        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    # Click on the profile to redirect More menu
    def test_redirect_more_menu(self):
        self.profile.redirect_more_menu()

    # Click on 'My Plan' to redirect Plan page
    def test_redirect_plan_page(self):
        self.profile.redirect_plan_page()


    # Select 'Monthly Plan'
    def test_select_monthly_plan(self,driver):
        try:

            # Locators and expected texts
            locators = [
                self.plan.GO_PREMIUM_HEADER_LOCATOR,
                self.plan.FREE_TRIAL_BENEFITS_LOCATOR,
            ]
            expected_texts = [
                self.plan.EXPECTED_GO_PREMIUM_HEADER_TEXT,
                self.plan.EXPECTED_FREE_TRIAL_BENEFITS_TEXT,
            ]

            #  Verify actual and expected text on the screen
            verify_text_on_screen(driver, locators, expected_texts)

            # Select the Monthly Plan
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.MONTHLY_PLAN_FIELD_LOCATOR)

        except Exception as e:
            logging.error(f"Error while activating free trial plan: {e}")
            pytest.fail(f"Failed to activate free trial plan: {e}")

    # Click on 'Pay Now' button
    def test_click_on_pay_button(self):
        try:
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.PAY_BUTTON_LOCATOR)
            logging.info("Clicked on Pay button.")
        except Exception as e:
            logging.error(f"Error while clicking on Pay button: {e}")

    def test_make_payment(self, driver):
        try:
            # Initialize WebDriverWait with the driver and timeout
            wait = WebDriverWait(driver, 30)  # Use the passed 'driver' argument

            # Wait until the element is visible using its XPath locator
            ele = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.razorpay.BRAND_NAME_LOCATOR)))

            # Get the Brand name
            brand_name = ele.get_attribute("text")
            print(f'\nBrand Name: {brand_name}')
            assert brand_name == 'Saregama India Ltd.'

            # Select payment type 'UPI'
            self.razorpay.wait_and_click(by=AppiumBy.XPATH, value=self.razorpay.UPI_FIELD_LOCATOR)

            # Click on the UPI text field
            self.razorpay.wait_and_click(by=AppiumBy.XPATH, value=self.razorpay.UPI_TEXT_FIELD_LOCATOR)

            # Wait for the UPI ID input field and enter UPI ID
            fill_upi_id = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.razorpay.UPI_TEXT_FIELD_LOCATOR)))
            fill_upi_id.send_keys(UPI_ID)

            # Click on 'Pay Now' button
            self.razorpay.wait_and_click(by=AppiumBy.XPATH, value=self.razorpay.PAY_NOW_BUTTON_LOCATOR)
            logging.info("Clicked on Pay Now button.")

        except Exception as e:
            logging.error(f"Error while making payment: {e}")

    # Click on 'Start Learning' button
    def test_click_start_learning(self):
        try:
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.click_start_learning)
            logging.info("Clicked on Start Learning button.")
        except Exception as e:
            logging.error(f"Error while clicking on Start Learning button: {e}")

# # Test for new user login and profile creation
    # @pytest.mark.skipif(USER_TYPE != 'NEW', reason="Skipped because USER_TYPE is not 'NEW'")
    # def test_login_and_create_user_profile(self):
    #     """Login as a new user and create a user profile."""
    #     try:
    #         logging.info("Starting login process...")
    #         self.login.click_sign_in()
    #         self.login.perform_login()
    #         logging.info("Login successful.")
    #
    #         # Create User Profile
    #         self.create_user_profile.enter_first_name(NEW_USER_FIRST_NAME)
    #         logging.info("Entered first name.")
    #         self.create_user_profile.select_voice_type(NEW_USER_VOICE_TYPE)
    #         logging.info("Voice type selected.")
    #
    #         scroll_down(self.driver)
    #         logging.info("Scrolled down the page.")
    #         self.create_user_profile.select_age(NEW_USER_AGE_GROUP)
    #         logging.info("Age selected.")
    #
    #         self.create_user_profile.select_skill_level(NEW_USER_SKILL_LEVEL)
    #         logging.info("Skill level selected.")
    #         self.create_user_profile.click_continue_button()
    #         logging.info("Clicked on Continue button.")
    #     except Exception as e:
    #         pytest.fail(f"Test failed: {e}")