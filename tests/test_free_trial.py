import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.free_trial_page import FreeTrialPage
from pages.login_page import LoginPage
from pages.more_page import MorePage
from pages.profile_page import ProfilePage

@pytest.mark.usefixtures("driver")
class TestFreeTrial:

    @pytest.fixture
    def setup_pages(self, driver):
        # Combine page objects into a single fixture
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.more_page = MorePage(driver)
        self.free_trial_page = FreeTrialPage(driver)

    def test_login(self, setup_pages):
        """Test case to perform login."""
        try:
            self.login_page.click_sign_in()
            self.login_page.click_on_field()
            self.login_page.perform_login('4444455555')
        except Exception as e:
            pytest.fail(f"Login test failed: {str(e)}")

    def test_select_profile(self, setup_pages):
        """Test case to select a profile after login."""
        try:
            self.profile_page.select_profile('Sameer Khan')
        except NoSuchElementException as e:
            pytest.fail(f"Profile selection failed: {str(e)}")

    def test_navigate_to_my_plan(self, setup_pages):
        """Test case to navigate to the 'My Plan' section."""
        try:
            self.more_page.click_more_menu()
            self.more_page.click_my_plan()
        except TimeoutException as e:
            pytest.fail(f"Navigation to 'My Plan' failed: {str(e)}")

    def test_activate_free_trial(self, setup_pages):
        """Test case to activate the free trial."""
        try:
            # Access the free_trial_page through setup_pages
            self.free_trial_page.select_plan_type()
            self.free_trial_page.verify_free_trial_activation()
            self.free_trial_page.click_start_learning()
            self.free_trial_page.verify_home_screen()
        except Exception as e:
            pytest.fail(f"Free trial activation test failed: {str(e)}")
