from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from uiautomator2.xpath import TimeoutException

from pages.base_class import BaseClass


class MorePage(BaseClass):
    MORE_MENU = (AppiumBy.ACCESSIBILITY_ID, 'More')
    MY_PLAN = (AppiumBy.ACCESSIBILITY_ID, 'My Plan')

    # Click on 'More' tab
    def click_more_menu(self):
        try:
            self.wait_and_click(*self.MORE_MENU)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error clicking on More tab")

    def click_my_plan(self):
        try:
            self.wait_and_click(*self.MY_PLAN)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Error clicking on My Plan")
