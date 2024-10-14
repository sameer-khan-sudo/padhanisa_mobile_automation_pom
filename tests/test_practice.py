from pages.practice_page import Practice
from pages.login_page import LoginPage
import pytest

@pytest.fixture(scope="class")
def setup(driver):
    practice_page = Practice(driver)
    login_page = LoginPage(driver)
    return practice_page

class TestPractice:

    # Select the 'Sing A Song' tab
    def test_select_practice_tab(self, setup):
        setup.select_practice_tab()

    # Click on the search icon
    def test_click_search_icon(self, setup):
        setup.click_search_icon()

    # Scroll through the song list and extract song details
    def test_scroll_and_extract_content(self, setup):
        reports = setup.test_scroll_and_extract_content()

        if reports:
            print("Extracted Song Details:")
            for report in reports:
                pass
                # print(len(reports))
        else:
            print("No song details extracted.")
