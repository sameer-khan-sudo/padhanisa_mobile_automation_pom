import pytest
from selenium.common import TimeoutException

from conftest import driver
from pages.create_profile import CreateProfile
from pages.free_trial_page import FreeTrialPage
from pages.login_page import LoginPage
from pages.more_page import MorePage
from pages.profile_page import ProfilePage
from utils.utils import tap_at_coordinates, scroll_down


@pytest.mark.usefixtures("driver")
class TestFreeTrial:

    @pytest.fixture
    def setup_pages(self, driver):
        # Initialize page objects
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.more_page = MorePage(driver)
        self.free_trial_page = FreeTrialPage(driver)
        self.create_profile = CreateProfile(driver)

    # Perform Login
    def test_login(self, setup_pages):
        try:
            self.login_page.click_sign_in()
            self.login_page.click_on_field()
            self.login_page.perform_login()
        except Exception as e:
            pytest.fail(f"Login test failed: {str(e)}")  # Fail the test with a detailed message

    # Create Profile
    def test_create_profile(self, setup_pages):
        try:
            # Enter first name
            self.create_profile.enter_first_name_field('Shadow')
            tap_at_coordinates(self)

            # Enter last name (uncomment if needed)
            # self.create_profile.enter_last_name_field('User')
            # tap_at_coordinates(self)

            # Select voice type
            self.create_profile.select_voice_type()

            # Select age
            self.create_profile.select_age('16')

            # Scroll forward in the scrollable view
            scroll_down(self)

            # Select skill level
            self.create_profile.select_skill_level('Never Learnt Before')

            # Enter email id
            self.create_profile.enter_email_id('crypto@gmail.com')
            tap_at_coordinates(self)

            # Click on continue button
            self.create_profile.click_on_continue_button()

        except Exception as e:
            pytest.fail(f"Profile creation test failed: {str(e)}")  # Fail the test with a detailed message

    # Navigate to the 'My Plan' section.
    def test_navigate_to_my_plan(self, setup_pages):
        try:
            self.more_page.click_more_menu()
            self.more_page.click_my_plan()
        except TimeoutException as e:
            pytest.fail(f"Navigation to 'My Plan' failed: {str(e)}")
