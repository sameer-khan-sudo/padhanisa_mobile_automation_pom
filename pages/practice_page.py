import json
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_class import BaseClass


class Practice(BaseClass):
    # Locators for elements
    SING_A_SONG_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Sing A Song")')
    SEARCH_ICON_LOCATOR = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
    FILTER_BUTTON_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Filter")')

    def select_practice_tab(self):
        # Click on the 'Sing A Song' tab
        self.wait_and_click(*self.SING_A_SONG_LOCATOR)

    def click_search_icon(self):
        self.wait_and_click(*self.SEARCH_ICON_LOCATOR)

    # Scroll the global search song list and extract the data
    def test_scroll_and_extract_content(self):
        try:
            # SONG_LIST_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc]')
            SONG_LIST_LOCATOR = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')

            all_elements = []
            previous_element_descs = set()  # Keep track of content descriptions we've processed
            last_element_reached = False

            while not last_element_reached:
                # Wait for the visible elements to load
                try:
                    visible_elements = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located(SONG_LIST_LOCATOR)
                    )
                    print(f"Visible elements found: {len(visible_elements)}")
                except TimeoutException:
                    print("Elements not found after scrolling.")
                    break

                # Filter out elements that have already been processed
                new_elements = [elem for elem in visible_elements
                                if elem.get_attribute('content-desc') not in previous_element_descs]

                if not new_elements:
                    last_element_reached = True
                    print("Reached the last element in the list.")
                else:
                    for elem in new_elements:
                        content = elem.get_attribute('content-desc')
                        print(f"Element content description: {content}")  # Debugging output
                        if content:
                            all_elements.append(content)
                            previous_element_descs.add(content)

                    # Perform scroll action
                    self.driver.swipe(100, 1000, 100, 200, 1000)
                    print("Performed scroll.")

            if not all_elements:
                print("No elements were collected.")
                return

            # Process the collected elements and extract the song details
            reports = []
            for i, content in enumerate(all_elements):
                # Assuming the content-desc format is "Song Name\nSinger Name\nRange\nDifficulty"
                parts = content.split('\n')
                report = {
                    "Index": i + 1,
                    "Song Name": parts[0] if len(parts) > 0 else "N/A",
                    "Singer Name": parts[1] if len(parts) > 1 else "N/A",
                    "Range": parts[2] if len(parts) > 2 else "N/A",
                    "Difficulty Type": parts[3] if len(parts) > 3 else "N/A"
                }
                reports.append(report)

            # Print the total count and the formatted reports in JSON
            print(f"Total songs extracted: {len(reports)}")
            # print(json.dumps(reports, indent=4))

            return reports

        except NoSuchElementException as e:
            print(f"Element not found: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
