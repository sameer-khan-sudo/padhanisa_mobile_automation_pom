import time
from typing import List, Dict

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver
from pages.base_class import BaseClass

class Practice(BaseClass):
    # Locators for elements
    SING_A_SONG_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Sing A Song")')
    SEARCH_ICON_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
    FILTER_BUTTON_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Filter")')
    SONG_LIST_LOCATOR = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View')
    GLOBAL_SEARCH_SONG_LIST_LOCATOR = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')

    def select_practice_tab(self):
        self.wait_and_click(*self.SING_A_SONG_LOCATOR)

    def click_search_icon(self):
        self.wait_and_click(*self.SEARCH_ICON_LOCATOR)

    def scroll_and_extract_songs(self, locator: tuple) -> List[Dict[str, str]]:
        all_elements = []
        previous_element_descs = set()
        last_element_reached = False

        while not last_element_reached:
            try:
                visible_elements = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(locator)
                )
            except TimeoutException:
                print("Elements not found after scrolling.")
                break

            new_elements = [elem for elem in visible_elements
                            if elem.get_attribute('content-desc') not in previous_element_descs]

            if not new_elements:
                last_element_reached = True
                print("Reached the last element in the list.")
            else:
                for elem in new_elements:
                    content = elem.get_attribute('content-desc')
                    if content:
                        all_elements.append(content)
                        previous_element_descs.add(content)

                self.driver.swipe(100, 1000, 100, 200, 1000)
                time.sleep(1)  # Added 1-second wait after each scroll

        return self.process_song_data(all_elements)

    @staticmethod
    def process_song_data(elements: List[str]) -> List[Dict[str, str]]:
        reports = []
        for i, content in enumerate(elements):
            parts = content.split('\n')
            report = {
                "Index": i + 1,
                "Song Name": parts[0] if len(parts) > 0 else "N/A",
                "Singer Name": parts[1] if len(parts) > 1 else "N/A",
                "Range": parts[2] if len(parts) > 2 else "N/A",
                "Difficulty Type": parts[3] if len(parts) > 3 else "N/A"
            }
            reports.append(report)
        return reports

    @pytest.mark.usefixtures("driver")
    def test_scroll_song_list(self):
        try:
            reports = self.scroll_and_extract_songs(self.SONG_LIST_LOCATOR)
            print(f"Total songs extracted: {len(reports)}")
            return reports
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def test_scroll_and_extract_content(self):
        try:
            reports = self.scroll_and_extract_songs(self.GLOBAL_SEARCH_SONG_LIST_LOCATOR)
            print(f"Total songs extracted: {len(reports)}")
            return reports
        except Exception as e:
            print(f"An error occurred: {str(e)}")