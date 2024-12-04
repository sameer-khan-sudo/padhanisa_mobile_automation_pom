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

# Test Data
USER_TYPE = 'EXIST'
EXISTING_USER_PHONE = '1100000000'
# PROFILE_NAME = 'Strange'
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
            time.sleep(2)

        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    # Redirect More section / Click on Profile icon
    def test_redirect_more_menu(self):
        try:
            # Get the profile name
            name = PROFILE_NAME[0]
            # print('Name : ', name)

            # Check if the profile letter locator is visible
            profile_letter_locator = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc,"{name}")]'))
            )
            print("Profile Letter Locator is found")
        except TimeoutException:
            profile_letter_locator = None

        try:
            # Check if the profile image locator is visible
            profile_image_locator = self.wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'))
            )
            print("Profile Image Locator is found")
        except TimeoutException:
            profile_image_locator = None

        # Perform the click operation
        if profile_letter_locator:
            print("Clicking on Profile Letter Locator")
            profile_letter_locator.click()
        elif profile_image_locator:
            print("Clicking on Profile Image Locator")
            profile_image_locator.click()
        else:
            print("Neither locator is found. Test cannot proceed.")
