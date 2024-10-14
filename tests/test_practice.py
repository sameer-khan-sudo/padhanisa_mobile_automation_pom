import pytest
from conftest import driver
from pages.create_profile import CreateProfile
from pages.PLAN_PAGES.free_trial_page import FreeTrialPage
from pages.login_page import LoginPage
from pages.more_page import MorePage
from pages.practice_page import Practice
from pages.profile_page import ProfilePage
from utils.utils import scroll_down, hide_keyboard  # Removed unused import click_start_learning

@pytest.mark.usefixtures("driver")
class TestPractice:

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        # Initialize page objects
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.practice_page = Practice(driver)

    def test_login(self):
        # Perform login action
        self.login_page.click_sign_in()
        self.login_page.click_on_field()
        self.login_page.exist_user_login()

    # Select user profile
    def test_select_user_profile(self):
        # Select a specific user profile
        self.profile_page.select_profile('SAM')

    # Click on 'Sing A Song' tab
    def test_click_practice_tab(self):
        # Navigate to the Practice tab
        self.practice_page.select_practice_tab()

    # Click on the 'Search' icon
    def test_click_search_icon(self):
        # Navigate to the Practice tab
        self.practice_page.click_search_icon()

