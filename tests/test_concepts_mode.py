import time
import pytest
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

    def test_scroll(self):
        self.concepts_mode_page.scroll_video_list()
