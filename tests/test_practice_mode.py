import pytest
from pages.practice_mode_page import PracticeModePage

class TestPracticeMode:
    @pytest.fixture(autouse=True)

    # Initialize objects
    def setup(self, driver):
        self.practice_mode_page = PracticeModePage(driver)

    # Click on 'Skip' button
    def test_click_skip(self):
        self.practice_mode_page.click_skip()

    def test_print(self):
        pass




