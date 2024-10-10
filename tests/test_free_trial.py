import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from conftest import driver
from pages.create_profile import CreateProfile
from pages.free_trial_page import FreeTrialPage
from pages.login_page import LoginPage
from pages.more_page import MorePage
from pages.profile_page import ProfilePage
from utils.utils import tap_at_coordinates, scroll_down, hide_keyboard, click_start_learning, get_formatted_expiry_date


@pytest.mark.usefixtures("driver")
class TestFreeTrial:

    @pytest.fixture
    def setup_pages(self, driver):
        # Initialize page objects.
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.more_page = MorePage(driver)
        self.free_trial_page = FreeTrialPage(driver)
        self.create_profile = CreateProfile(driver)

    # Perform login action.
    def test_login(self, setup_pages):
        try:
            self.login_page.click_sign_in()
            self.login_page.click_on_field()
            self.login_page.perform_login()
        except Exception as e:
            pytest.fail(f"Login test failed: {str(e)}")

    # Create a profile.
    def test_create_profile(self, setup_pages):
        try:
            self.create_profile.enter_first_name_field('Shadow')
            hide_keyboard(self)

            # Optionally enter last name
            # self.create_profile.enter_last_name_field('User')

            self.create_profile.select_voice_type()
            self.create_profile.select_age('16')
            scroll_down(self)
            self.create_profile.select_skill_level('Never Learnt Before')
            # self.create_profile.enter_email_id('crypto@gmail.com')
            # hide_keyboard(self)
            tap_at_coordinates(self)
            self.create_profile.click_on_continue_button()
        except Exception as e:
            pytest.fail(f"Profile creation test failed: {str(e)}")

    # Navigate to 'My Plan' section.
    def test_navigate_to_my_plan(self, setup_pages):
        try:
            self.more_page.click_more_menu()
            self.more_page.click_my_plan()
        except TimeoutException as e:
            pytest.fail(f"Navigation to 'My Plan' failed: {str(e)}")

    # Select the 'Free Trial' plan.
    def test_select_trial_plan(self, setup_pages):
        try:
            self.free_trial_page.select_trial_plan()
        except TimeoutException as e:
            pytest.fail(f"Failed to select Free Trial plan: {str(e)}")

    # Click the 'Continue' button after selecting a free trial plan.
    def test_click_on_continue_button(self, setup_pages):
        try:
            self.free_trial_page.click_continue()
            self.free_trial_page.verify_free_trial_activation()


        except TimeoutException as e:
            pytest.fail(f"Failed to click on 'Continue' button: {str(e)}")
    # @pytest.mark.skip
    # # Click on 'Start Learning' button
    # def test_click_on_start_learning(self,setup_pages):
    #     try:
    #         click_start_learning(self)
    #     except TimeoutException as e:
    #         pytest.fail(f"Failed to click on 'Start Learning' button: {str(e)}")
    #
    #
