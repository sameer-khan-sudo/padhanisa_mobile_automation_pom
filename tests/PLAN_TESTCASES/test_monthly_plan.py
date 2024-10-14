import pytest
from conftest import driver
from pages.create_profile import CreateProfile
from pages.PLAN_PAGES.free_trial_page import FreeTrialPage
from pages.login_page import LoginPage
from pages.more_page import MorePage
from pages.profile_page import ProfilePage
from utils.utils import scroll_down, hide_keyboard  # Removed click_start_learning
from pages.PLAN_PAGES.monthly_plan_page import MonthlyPlanPage

# Automatically use the "driver" fixture for this test function
@pytest.mark.usefixtures("driver")
class TestFreeTrial:

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        # Initialize page objects.
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.more_page = MorePage(driver)
        self.free_trial_page = FreeTrialPage(driver)
        self.create_profile = CreateProfile(driver)
        self.monthly_plan_page = MonthlyPlanPage(driver)

    user_login_type = 'Exist'
    if user_login_type == 'New':
        # Perform login action.
        def test_login(self):
            self.login_page.click_sign_in()
            self.login_page.click_on_field()
            self.login_page.perform_login()

        # Create a profile.
        def test_create_profile(self):
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

    elif user_login_type == 'Exist':

        # Perform login
        def test_login(self):
            self.login_page.click_sign_in()
            self.login_page.click_on_field()
            self.login_page.exist_user_login()

        # Select user profile
        def test_select_profile(self):
            self.profile_page.select_profile('SAM')


    # Navigate to 'My Plan' section.
    def test_navigate_to_my_plan(self):
        self.more_page.click_more_menu()
        self.more_page.click_my_plan()

    # Select the 'Monthly Trial' plan.
    def test_select_trial_plan(self):
        self.monthly_plan_page.select_monthly_plan()

    # Click on 'Proceed to Pay' button
    def test_click_pay_button(self):
        self.monthly_plan_page.click_pay_button()