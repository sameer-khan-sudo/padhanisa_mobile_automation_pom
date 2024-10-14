from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
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