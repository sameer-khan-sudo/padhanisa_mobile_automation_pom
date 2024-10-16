import json

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BasePage

class ConceptsMode(BasePage):
    CONCEPTS_MODE_TAB_LOCATOR = (AppiumBy.XPATH, '//android.widget.ImageView[contains(@content-desc,"Concepts")]')
    SEARCH_BAR_ICON_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
    VIDEO_LIST_LOCATOR = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')

    # Select 'Concepts' tab
    def select_concept_mode(self):
        # Scroll forward
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollForward()'
        )
        # Perform click
        self.wait_and_click(*self.CONCEPTS_MODE_TAB_LOCATOR)


    def scroll_video_list(self):
        container_locator = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View')
        element_locator = (AppiumBy.XPATH, "//android.view.View[1]//android.view.View[contains(@content-desc, ' ')]")

        all_elements = []
        print(type(all_elements))
        last_element_reached = False
        previous_elements = []

        while not last_element_reached:
            visible_elements = self.driver.find_elements(*element_locator)

            new_elements = [elem for elem in visible_elements if elem not in previous_elements]
            if not new_elements:
                last_element_reached = True
                print("Reached the last element in the list.")
            else:
                for elem in new_elements:
                    content = elem.get_attribute("content-desc")
                    all_elements.append(content)

                previous_elements = visible_elements
                container_element = self.driver.find_element(*container_locator)
                self.driver.execute_script('mobile: scrollGesture', {
                    'elementId': container_element.id,
                    'direction': 'down',
                    'percent': 3.0
                })

        # Process and format the collected data
        reports = [{"Index ": i + 1, "Video Name ": content} for i, content in enumerate(all_elements)]

        # Print reports in JSON format
        print(json.dumps(reports, indent=4))
        print("Count of Concepts Videos :", len(reports))

        return reports
