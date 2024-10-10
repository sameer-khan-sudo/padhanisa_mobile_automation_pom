import pytest
from selenium.common import TimeoutException, NoSuchElementException

from conftest import driver
from pages.create_profile import CreateProfile
from pages.free_trial_page import FreeTrialPage
from pages.login_page import LoginPage
from pages.more_page import MorePage
from pages.profile_page import ProfilePage
from utils.utils import scroll_down, hide_keyboard, click_start_learning

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
        self.login_page.click_sign_in()
        self.login_page.click_on_field()
        self.login_page.perform_login()

    # Create a profile.
    def test_create_profile(self, setup_pages):
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
        self.create_profile.click_on_continue_button()

    # Navigate to 'My Plan' section.
    def test_navigate_to_my_plan(self, setup_pages):
        self.more_page.click_more_menu()
        self.more_page.click_my_plan()

    # Select the 'Free Trial' plan.
    def test_select_trial_plan(self, setup_pages):
        self.free_trial_page.select_trial_plan()

    # Click the 'Continue'
    def test_click_on_continue_button(self, setup_pages):
        self.free_trial_page.click_continue()

    # Verify success message and expiry
    def test_verify_expiry_and_message(self, setup_pages):
        self.free_trial_page.verify_free_trial_activation()
        # self.free_trial_page.verify_home_screen()

    # Click on 'Start Learning' button
    def test_click_on_start_learning(self, setup_pages):
        click_start_learning(self)

    def test_verify_home_screen_redirection(self, setup_pages):
        self.free_trial_page.verify_screen_redirection('More')
