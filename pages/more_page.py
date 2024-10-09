from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass

class MorePage(BaseClass):
    MORE_MENU = (AppiumBy.ACCESSIBILITY_ID, 'More')
    MY_PLAN = (AppiumBy.ACCESSIBILITY_ID, 'My Plan')

    def click_more_menu(self):
        self.wait_and_click(*self.MORE_MENU)

    def click_my_plan(self):
        self.wait_and_click(*self.MY_PLAN)