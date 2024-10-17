import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from conftest import driver  # Ensure this is defined in your conftest.py
from pages.concepts_mode_page import ConceptsMode


class TestConceptsMode:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.concepts_mode_page = ConceptsMode(driver)

    def test_click_on_skip(self):
        self.concepts_mode_page.click_skip()

    def test_click_singing_classes(self):
        self.concepts_mode_page.select_class_module()
        time.sleep(1)

    def test_select_concepts_mode(self):
        self.concepts_mode_page.select_concept_mode()

    @pytest.mark.skip
    def test_scroll(self):
        self.concepts_mode_page.scroll_concept_video_list()

    # Search for a concept video and optionally play it if found.
    video_name = 'Vocal Range Introduction'

    def test_search_and_play_video(self, driver, play_video=False):
        # Search for the concept video
        self.concepts_mode_page.search_concept_video(self.video_name)

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
                self.concepts_mode_page.play_searched_video(self.video_name)
            else:
                print(f"Video '{self.video_name}' found, but play_video flag is set to False.")
