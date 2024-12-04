import json
import logging  # For logging test execution details.
import time

import pytest  # For writing and managing tests.
from appium.webdriver.common.appiumby import AppiumBy  # Appium-specific locators.
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver  # Shared driver setup.
from pages.create_profile_page import CreateProfile  # Page object for "Create Profile".
from pages.login_page import LoginPage  # Page object for "Login".
from pages.plan_page import PlanPage  # Page object for "Plan".
from pages.profile_page import ProfilePage, get_first_letter  # Page object for "Profile".
from pages.razor_pay_page import RazorPayPage
from utils.helpers import verify_text_on_screen, scroll_down  # Helper functions for scrolling and text verification.

# Configure logging
logging.basicConfig(level=logging.INFO)

# Test Data Configuration
# Choose between 'EXIST' and 'NEW'
USER_TYPE = 'NEW'

UPI_ID = 'success@razorpay'

# Load test data from JSON
with open('C:/Users/khans/PycharmProjects/padhanisa_automation_pom/test_data/profile_data.json') as test_data_file:
    profile_data = json.load(test_data_file)

# Extract data based on user type
if USER_TYPE == 'EXIST':
    EXISTING_USER_PHONE = profile_data['existUserProfileData']['existingUserPhone']
    PROFILE_NAME = profile_data['existUserProfileData']['profileName']
else:  # NEW user
    NEW_USER_FIRST_NAME = profile_data['newUserProfileData']['firstName']
    NEW_USER_VOICE_TYPE = profile_data['newUserProfileData']['voiceType']
    NEW_USER_AGE_GROUP = profile_data['newUserProfileData']['ageGroup']
    NEW_USER_SKILL_LEVEL = profile_data['newUserProfileData']['skillLevel']

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
    @pytest.mark.skipif(USER_TYPE != 'EXIST', reason="Skipped because USER_TYPE is not 'NEW")
    def test_perform_exist_user_login(self):
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

    # Login with new user by creating new profile
    @pytest.mark.skipif(USER_TYPE != 'NEW', reason="Skipped because USER_TYPE is not 'EXIST'")
    def test_login_and_create_user_profile(self):
        try:
            logging.info("Starting login process...")
            self.login.click_sign_in()
            self.login.perform_login()
            logging.info("Login successful.")

            # Create User Profile
            self.create_user_profile.enter_first_name(NEW_USER_FIRST_NAME)
            logging.info("Entered first name.")

            self.create_user_profile.select_voice_type(NEW_USER_VOICE_TYPE)
            logging.info("Voice type selected.")

            scroll_down(self.driver)
            logging.info("Scrolled down the page.")
            self.create_user_profile.select_age(NEW_USER_AGE_GROUP)
            logging.info("Age selected.")

            self.create_user_profile.select_skill_level(NEW_USER_SKILL_LEVEL)
            logging.info("Skill level selected.")
            self.create_user_profile.click_continue_button()
            logging.info("Clicked on Continue button.")
            time.sleep(1)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    # Redirect More section / Click on Profile icon
    def test_redirect_more_menu(self):
        try:
            # Determine which profile name to use
            profile_name = (
                profile_data['existUserProfileData']['profileName']
                if USER_TYPE == 'EXIST'
                else profile_data['newUserProfileData']['firstName'][0]
            )

            # Check if the profile letter locator is visible
            profile_letter_locator = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc,"{profile_name}")]')
                )
            )
        except TimeoutException:
            profile_letter_locator = None
            print("Profile Letter Locator is not found")

        try:
            # Check if the profile image locator is visible
            profile_image_locator = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]')
                )
            )
            print("Profile Image Locator is found")
        except TimeoutException:
            profile_image_locator = None

        # Perform the click operation based on available locator
        if profile_letter_locator:
            profile_letter_locator.click()
        elif profile_image_locator:
            profile_image_locator.click()
        else:
            print("Neither locator is found. Test cannot proceed.")

    # Click on 'My Plan' to redirect Plan page
    def test_redirect_plan_page(self):
        self.profile.select_my_plan_option()

    # Select 'Monthly Plan'
    def test_select_monthly_plan(self, driver):
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
    # @pytest.mark.skip
    def test_click_on_pay_button(self):
        try:
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.PAY_BUTTON_LOCATOR)
            logging.info("Clicked on Pay button.")
        except Exception as e:
            logging.error(f"Error while clicking on Pay button: {e}")

    # Make payment using RazorPay
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
    @pytest.mark.skip
    def test_click_start_learning(self):
        try:
            self.plan.wait_and_click(AppiumBy.XPATH, value=self.plan.click_start_learning)
            logging.info("Clicked on Start Learning button.")
        except Exception as e:
            logging.error(f"Error while clicking on Start Learning button: {e}")