import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from conftest import driver  # Ensure this is defined in your conftest.py
from pages.concepts_mode_page import ConceptsMode

class TestConceptsMode:
    @pytest.fixture(autouse=True)
    def setup(self, driver):  # Ensure you have a driver fixture in conftest.py
        self.driver = driver  # Store driver in the instance
        self.concepts_mode_page = ConceptsMode(driver)

    # Click on 'Skip' button
    def test_click_on_skip(self):
        self.concepts_mode_page.click_skip()

    # Click 'Singing Classes' tab
    def test_click_singing_classes(self):
        self.concepts_mode_page.select_class_module()
        time.sleep(1)

    # Test to select 'Concepts' mode
    def test_select_concepts_mode(self):
        self.concepts_mode_page.select_concept_mode()

    @pytest.mark.skip
    def test_scroll(self):
        self.concepts_mode_page.scroll_concept_video_list()

    # Define video_name at the class level to reuse it across multiple tests
    video_name = 'Sur Introduction'

    # Search concept video
    def test_search_video(self,driver):
        # Search for the concept video
        self.concepts_mode_page.search_concept_video(self.video_name)

        # Define the locator for "No Result Found"
        no_result_found_locator = (AppiumBy.XPATH, '//android.view.View[@content-desc="No Result Found"]')

        try:
            # Check if "No Result Found" is displayed
            no_result_element = driver.find_element(*no_result_found_locator)
            if no_result_element.is_displayed():
                print("No result found")
                return
        except NoSuchElementException:
            print("Results found")

        # Call the play function if results are found
        self.play_searched_video(self.video_name)

    def play_searched_video(self, video_name):
        # Play the searched video
        self.concepts_mode_page.play_searched_video(video_name)