import json
import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BasePage

class ConceptsMode(BasePage):
    CONCEPTS_MODE_TAB_LOCATOR = (AppiumBy.XPATH, '//android.widget.ImageView[contains(@content-desc,"Concepts")]')
    SEARCH_BAR_ICON_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
    # VIDEO_LIST_LOCATOR = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    # VIDEO_LIST_LOCATOR = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View')

    # Select 'Concepts' tab
    def select_concept_mode(self):
        # Scroll forward
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollForward()'
        )
        # Perform click
        self.wait_and_click(*self.CONCEPTS_MODE_TAB_LOCATOR)

    # def scroll_video_list(self):
    #     self.wait_and_click(*self.SEARCH_BAR_ICON_LOCATOR)
    #     time.sleep(2)
    #
    #     container_locator = (AppiumBy.ANDROID_UIAUTOMATOR,
    #                          'new UiSelector().className("android.view.View").instance(10)')
    #     element_locator = (AppiumBy.XPATH, "//android.view.View[1]//android.view.View[contains(@content-desc, ' ')]")
    #
    #     all_elements = []  # List to store content descriptions
    #     last_element_reached = False
    #     previous_element_count = 0
    #
    #     while not last_element_reached:
    #         # Extract content descriptions
    #         try:
    #             visible_elements = self.driver.find_elements(*element_locator)
    #         except Exception as e:
    #             print(f"Error finding elements: {e}")
    #             break
    #
    #         if not visible_elements:
    #             print("No elements found in this scroll.")
    #             break
    #
    #         # Collect content descriptions from visible elements
    #         for elem in visible_elements:
    #             content = elem.get_attribute("content-desc")
    #             if content:
    #                 all_elements.append(content)  # Add to the list
    #
    #         # Remove duplicates if any (optional)
    #         all_elements = list(dict.fromkeys(all_elements))
    #
    #         # Check if the number of elements has increased after scrolling
    #         if len(all_elements) == previous_element_count:
    #             last_element_reached = True
    #             print("No more new elements found, stopping scroll.")
    #             break
    #
    #         # Update previous element count to track new additions
    #         previous_element_count = len(all_elements)
    #
    #         # Use UiScrollable to scroll down the container
    #         try:
    #             scrollable = 'new UiScrollable(new UiSelector().className("android.view.View").instance(10)).scrollForward()'
    #             self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable)
    #         except Exception as e:
    #             print(f"Error during scrolling with UiScrollable: {e}")
    #             break
    #
    #         # Wait for elements to load
    #         time.sleep(3)
    #
    #     # Process and format the collected data
    #     reports = [{"Index": i + 1, "Video Name": content} for i, content in enumerate(all_elements)]
    #
    #     # Print reports in JSON format
    #     print(json.dumps(reports, indent=4))
    #     print("Total Count of Videos:", len(reports))
    #
    #     return reports

    def scroll_video_list(self):
        self.wait_and_click(*self.SEARCH_BAR_ICON_LOCATOR)
        time.sleep(2)

        element_locator = (AppiumBy.XPATH, "//android.view.View[1]//android.view.View[contains(@content-desc, ' ')]")
        scroll_command = 'new UiScrollable(new UiSelector().className("android.view.View").instance(10)).scrollForward()'

        all_elements = set()
        while True:
            try:
                visible_elements = self.driver.find_elements(*element_locator)
                new_elements = {elem.get_attribute("content-desc") for elem in visible_elements if
                                elem.get_attribute("content-desc")}

                if not new_elements or new_elements.issubset(all_elements):
                    break

                all_elements.update(new_elements)
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command)
                time.sleep(3)
            except Exception as e:
                print(f"Error: {e}")
                break

        reports = [{"Index": i + 1, "Video Name": content} for i, content in enumerate(all_elements)]
        print(json.dumps(reports, indent=4))
        print(f"Total Count of Concepts Videos: {len(reports)}")

        return reports