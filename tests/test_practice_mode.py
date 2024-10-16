import time

import pytest
from pages.practice_mode_page import PracticeModePage

class TestPracticeMode:
    @pytest.fixture(autouse=True)

    # Initialize objects
    def setup(self, driver):
        self.practice_mode_page = PracticeModePage(driver)

    # Click on 'Skip' button
    def test_click_on_skip(self):
        self.practice_mode_page.click_skip()

    # Select 'Sing A Song' tab
    def test_select_practice_mode(self):
        self.practice_mode_page.select_practice_mode()
        time.sleep(1)




