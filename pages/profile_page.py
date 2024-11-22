from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass
from selenium.common.exceptions import NoSuchElementException


class ProfilePage(BaseClass):

    MORE_MENU_LOCATOR = 'new UiSelector().className("android.widget.ImageView").instance(2)'
    MY_PLAN_LOCATOR = '//android.widget.ImageView[@content-desc="My Plan"]'

    def select_profile(self, profile_name):
        # Using the profile name to build the locator dynamically
        profile_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{profile_name}")')

        try:
            profile_element = self.driver.find_element(*profile_locator)
            if profile_element.is_displayed():
                self.wait_and_click(*profile_locator)
                print(f'Selected profile : {profile_name}')
        except NoSuchElementException:
            # Raising an exception to stop the test execution
            print(f'Profile with the name {profile_name} is not found. Stopping test execution.')
            raise Exception(f'Profile with the name {profile_name} is not found. Test stopped.')

    def redirect_more_menu(self):
        # Click on the profile to redirect More menu
        self.wait_and_click(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.MORE_MENU_LOCATOR)

    def redirect_plan_page(self):
        # Click on the More menu to redirect Plan page
        self.wait_and_click(by=AppiumBy.XPATH, value=self.MY_PLAN_LOCATOR)
