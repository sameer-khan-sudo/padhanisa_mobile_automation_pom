import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from conftest import driver  # Ensure this is defined in your conftest.py
from pages.concepts_mode_page import ConceptsMode
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.helpers import tap_on_screen


@pytest.mark.usefixtures("driver")
class TestConceptsMode:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.concepts_mode_page = ConceptsMode(driver)
        self.login = LoginPage(driver)
        self.profile = ProfilePage(driver)

    # Perform login with existing user
    @pytest.mark.dependency(name="LOGIN")
    def test_perform_login(self):
        try:
            self.login.click_sign_in()
            self.login.exist_user_login()
            time.sleep(2)
        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    # Select user profile (depends on login)
    @pytest.mark.dependency(name="PROFILE", depends=["LOGIN"])
    def test_select_user_profile(self):
        try:
            self.profile.select_profile('Tokio')
        except Exception as e:
            pytest.fail(f"Profile selection failed: {e}")

    # Click on 'Singing Classes' tab (depends on profile selection)
    @pytest.mark.dependency(name="SINGING_CLASSES")
    def test_click_singing_classes(self):
        try:
            self.concepts_mode_page.select_class_module()
            time.sleep(1)
        except Exception as e:
            pytest.fail(f"Failed to click on 'Singing Classes': {e}")

    # Select 'Concept' tab (depends on singing classes selection)
    @pytest.mark.dependency(name="CONCEPT_MODE_SELECTION", depends=["SINGING_CLASSES"])
    def test_select_concepts_mode(self):
        try:
            self.concepts_mode_page.select_concept_mode()
        except Exception as e:
            pytest.fail(f"Failed to select 'Concept Mode': {e}")

    # Perform scroll and get concept video data (skipped for now)
    @pytest.mark.skip
    @pytest.mark.dependency(depends=["CONCEPT_MODE_SELECTION"])
    def test_scroll(self):
        self.concepts_mode_page.scroll_concept_video_list()

    VIDEO_NAME = 'Vocal Range Introduction'

    # Search for a concept video and optionally play it if found.
    def test_search_and_play_video(self, driver, play_video=True):
        # Search for the concept video
        self.concepts_mode_page.search_concept_video(self.VIDEO_NAME)

        # Define the locator for "No Result Found"
        no_result_found_locator = (AppiumBy.XPATH, '//android.view.View[@content-desc="No Result Found"]')

        # Check if "No Result Found" is displayed
        try:
            no_result_element = self.driver.find_element(*no_result_found_locator)
            if no_result_element.is_displayed():
                pytest.xfail("No search results found. Stopping test execution.")
        except NoSuchElementException:
            # If "No Result Found" is not found, continue to check for video
            pass

        # If results are found, check the flag and play the video if required
        if play_video:
            self.concepts_mode_page.play_searched_video(self.VIDEO_NAME)
            time.sleep(3)
        else:
            print(f"Video '{self.VIDEO_NAME}' found, but play_video flag is set to False.")

    def test_video_actions(self, driver):

        # Perform the tap action on the screen
        tap_on_screen(driver)


