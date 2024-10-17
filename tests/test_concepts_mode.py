import time
from profile import Profile

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from conftest import driver  # Ensure this is defined in your conftest.py
from pages.concepts_mode_page import ConceptsMode
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestConceptsMode:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.concepts_mode_page = ConceptsMode(driver)
        self.login = LoginPage(driver)
        self.profile = ProfilePage(driver)

    # Perform login with existing user
    def test_perform_login(self):
        self.login.click_sign_in()
        self.login.exist_user_login()

    # Select user profile
    def test_select_user_profile(self):
        self.profile.select_profile('Sameer Khan')

    # Click on 'Singing Classes' tab
    def test_click_singing_classes(self):
        self.concepts_mode_page.select_class_module()
        time.sleep(1)

    # Select 'Concept' tab
    def test_select_concepts_mode(self):
        self.concepts_mode_page.select_concept_mode()

    # Perform scroll and get concept video data
    @pytest.mark.skip
    def test_scroll(self):
        self.concepts_mode_page.scroll_concept_video_list()

    VIDEO_NAME = 'Vocal Range Introduction'

    # Search for a concept video and optionally play it if found.
    def test_search_and_play_video(self,driver, play_video=True):
        # Search for the concept video
        self.concepts_mode_page.search_concept_video(self.VIDEO_NAME)

        # Define the locator for "No Result Found"
        no_result_found_locator = (AppiumBy.XPATH, '//android.view.View[@content-desc="No Result Found"]')

        # Check if "No Result Found" is displayed
        try:
            no_result_element = self.driver.find_element(*no_result_found_locator)
            if no_result_element.is_displayed():
                print("No result found")
                pytest.xfail("No search results found. Stopping test execution.")
        except NoSuchElementException:
            print("Results found")
            # If results are found, check the flag and play the video if required
            if play_video:
                self.concepts_mode_page.play_searched_video(self.VIDEO_NAME)
            else:
                print(f"Video '{self.VIDEO_NAME}' found, but play_video flag is set to False.")

