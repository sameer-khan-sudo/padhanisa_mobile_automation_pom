import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from pages.login_page import LoginPage
from pages.practice_mode_page import PracticeModePage
from pages.profile_page import ProfilePage


class TestPracticeMode:
    @pytest.fixture(autouse=True)

    # Initialize objects
    def setup(self, driver):
        self.practice_mode_page = PracticeModePage(driver)
        self.login = LoginPage(driver)
        self.profile = ProfilePage(driver)
        self.driver = driver

    # Click on 'Skip' button
    def test_click_on_skip(self,driver):
        self.practice_mode_page.click_skip()



    # Select 'Sing A Song' tab
    # def test_select_practice_mode(self):
    #     self.practice_mode_page.select_practice_mode()
    #     time.sleep(1)

    # Perform login with existing user
    # @pytest.mark.dependency(name="LOGIN")
    # def test_perform_login(self):
    #     try:
    #         self.login.click_sign_in()
    #         self.login.exist_user_login()
    #         time.sleep(2)
    #     except Exception as e:
    #         pytest.fail(f"Login failed: {e}")

