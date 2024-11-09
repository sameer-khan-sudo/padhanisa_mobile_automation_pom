import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from pages.create_profile_page import CreateProfile
from pages.login_page import LoginPage
from utils.helpers import scroll_down

# Configure logging
logging.basicConfig(level=logging.INFO)

@pytest.mark.usefixtures("driver")
class TestConceptsMode:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login = LoginPage(driver)
        self.create_user_profile = CreateProfile(driver)
        self.wait = WebDriverWait(driver, 10)  # Setting up an explicit wait

    # Perform login with existing user
    @pytest.mark.dependency(name="LOGIN")
    def test_perform_login(self):
        try:
            self.login.click_sign_in()
            self.login.perform_login()
            # Use WebDriverWait instead of sleep
            # self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Home")')))
            logging.info("Login successful.")
        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    def test_create_user_profile(self):
        try:
            logging.info("Starting profile creation...")

            # Enter first name
            self.create_user_profile.enter_first_name('Jack')
            logging.info("Entered first name.")

            # Enter last name
            self.create_user_profile.enter_last_name('Doe')
            logging.info("Entered last name.")

            # Select voice type
            self.create_user_profile.select_voice_type('Male')
            logging.info("Voice type selected.")

            # Scroll down
            scroll_down(self.driver)
            logging.info("Scrolled down the page.")

            # Select age
            self.create_user_profile.select_age('16 - 25')
            logging.info("Age selected.")

            # Select skill level
            self.create_user_profile.select_skill_level('I Am A Singer')
            logging.info("Skill level selected.")

            # Enter email
            self.create_user_profile.enter_email_id('test@gmail.com')
            logging.info("Entered email ID.")

        except Exception as e:
            pytest.fail(f"Profile creation failed: {e}")

    #   Click on Continue button
    def test_click_continue(self):
        try:
            self.create_user_profile.click_continue_button()
        except Exception as e:
            pytest.fail(f"Failed to click on Continue button: {e}")
