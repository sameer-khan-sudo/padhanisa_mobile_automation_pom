import logging
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from setuptools import setup

from conftest import driver
from pages.create_profile_page import CreateProfile
from pages.login_page import LoginPage
from pages.plan_page import PlanPage
from pages.profile_page import ProfilePage, get_first_letter
from pages.razor_pay_page import RazorPayPage
from utils.helpers import verify_text_on_screen, scroll_down

# Configure logging
logging.basicConfig(level=logging.INFO)

# Test Data
USER_TYPE = 'NEW'
EXISTING_USER_PHONE = '1100000000'
PROFILE_NAME = 'Jack'

NEW_USER_FIRST_NAME = 'SAM'
NEW_USER_VOICE_TYPE = 'Male'
NEW_USER_AGE_GROUP = '16 - 25'
NEW_USER_SKILL_LEVEL = 'I Am A Singer'
UPI_ID = 'success@razorpay'

# Test cases for Monthly Plan workflow
@pytest.mark.usefixtures("driver")
class TestFreeTrial:

    # Initialize the driver and page objects before each test.
    @pytest.fixture(autouse=True)
    def setup(self, driver):

        self.driver = driver
        self.login = LoginPage(driver)
        self.create_user_profile = CreateProfile(driver)
        self.plan = PlanPage(driver)
        self.profile = ProfilePage(driver)
        self.razorpay = RazorPayPage(driver)
        self.get_initial = None  # Initialize as a class attribute

    # Perform login and profile creation for new user
    @pytest.mark.skipif(USER_TYPE != 'NEW', reason="Skipped because USER_TYPE is not 'NEW'")
    def test_login_and_create_user_profile(self):
        try:
            logging.info("Starting login process...")
            self.login.click_sign_in()
            self.login.perform_login()
            logging.info("Login successful.")

            # Create User Profile
            self.create_user_profile.enter_first_name(NEW_USER_FIRST_NAME)
            logging.info(f"Entered first name: {NEW_USER_FIRST_NAME}")

            self.create_user_profile.select_voice_type(NEW_USER_VOICE_TYPE)
            logging.info(f"Voice type selected: {NEW_USER_VOICE_TYPE}")

            scroll_down(self.driver)
            logging.info("Scrolled down the page.")

            self.create_user_profile.select_age(NEW_USER_AGE_GROUP)
            logging.info(f"Age group selected: {NEW_USER_AGE_GROUP}")

            self.create_user_profile.select_skill_level(NEW_USER_SKILL_LEVEL)
            logging.info(f"Skill level selected: {NEW_USER_SKILL_LEVEL}")

            self.create_user_profile.click_continue_button()
            logging.info("Clicked on the Continue button.")

        except Exception as e:
            logging.error(f"An error occurred during profile creation: {e}")
            pytest.fail(f"Test failed due to error: {e}")


    # def test_redirect_more_menu(self):
    #     data = get_first_letter(NEW_USER_FIRST_NAME)
    #     print('Data:', data)
    #
    #     # Dynamic locator
    #     locator = f'//android.view.View/android.view.View[contains(@content-desc, "{data}")][1]'
    #
    #     try:
    #         # Check if the element is displayed and clickable
    #         element = self.driver.find_element(AppiumBy.XPATH, locator)
    #         if element.is_displayed():
    #             self.plan.wait_and_click(by=AppiumBy.XPATH, value=locator)
    #         else:
    #             print(f"Element with locator {locator} is not displayed.")
    #             raise Exception("Required element is not visible.")
    #     except Exception as e:
    #         print(f"Error in test_redirect_more_menu: {e}")
    #         raise

