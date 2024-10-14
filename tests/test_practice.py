# tests/test_practice.py
import time

import pytest

from conftest import driver
from pages.practice_page import Practice
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage  # Assuming this is also needed

@pytest.mark.usefixtures("driver")
class TestPractice:

    # Initialize page objects
    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.practice_page = Practice(driver)

    # Click on 'Skip' button
    def test_click_skip(self):
        print("Attempting to click the SKIP button...")
        self.login_page.click_skip()  # Corrected method name

    # Select the 'Sing A Song' tab
    def test_select_practice_tab(self):
        self.practice_page.select_practice_tab()
        time.sleep(2)

    # Scroll the song list
    def test_scroll_song_lis(self):
        self.practice_page.test_scroll_song_list()

    # Click on the search icon
    @pytest.mark.skip
    def test_click_search_icon(self):
        self.practice_page.click_search_icon()

    # Scroll the global search song list and extract song details
    @pytest.mark.skip
    def test_scroll_and_extract_global_search_songs(self):
        reports = self.practice_page.test_scroll_and_extract_content()

        if reports:
            for report in reports:
                pass
                # print(report)  # Printing each extracted report
        else:
            print("No song details extracted.")