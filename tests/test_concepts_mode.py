import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from conftest import driver
from pages.concepts_mode_page import ConceptsMode

class TestConceptsMode:
    @pytest.fixture(autouse=True)
    # Initialize objects
    def setup(self, driver):
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

    # @pytest.mark.skip
    # def test_scroll(self):
    #     self.concepts_mode_page.scroll_global_search_video_list()

    # Define video_name at the class level if you want to reuse it across multiple methods
    video_name = 'Sur Introduction'

    # Search concept video
    def test_search_video(self):
        self.concepts_mode_page.search_concept_video(self.video_name)
        no_result_found_locator = (AppiumBy.XPATH, '//android.view.View[@content-desc="No Result Found"]')
        if no_result_found_locator


    # Play the searched video
    def test_play_searched_video(self, video_name=video_name):
        self.concepts_mode_page.play_searched_video(video_name)

