from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass

class PracticePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def test_click_on_skip(self):
        self.click_on_skip()

