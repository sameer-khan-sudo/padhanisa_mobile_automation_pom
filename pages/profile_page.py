from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass


class ProfilePage(BaseClass):

    def select_profile(self, profile_name):
        # Using the profile name to build the locator dynamically
        profile_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{profile_name}")')
        self.wait_and_click(*profile_locator)
