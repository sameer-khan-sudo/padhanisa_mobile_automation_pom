from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass
from utils.utils import get_formatted_expiry_date


class MonthlyPlanPage(BaseClass):
    # SUCCESS_SCREEN_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Free Trial Activated"]')
    # HOME_SCREEN_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your Personal Singing Teacher"]')
    MONTHLY_PLAN_FIELD = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc,"Monthly")]')
    PAY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("TEST")')

    # YOUR_TEXT_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Your")')
    # DAYS_FREE_PREMIUM_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("14 Days Free Premium")')
    # IS_NOW_ACTIVE_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("is now active.")')

    # SUCCESS_SCREEN_HEADER_TEXT = 'Free Trial Activated'
    # YOUR_TEXT = 'Your'
    # DAYS_FREE_PREMIUM_TEXT = '14 Days Free Premium'
    # IS_NOW_ACTIVE_TEXT = 'is now active.'
    # HOME_SCREEN_HEADER_TEXT = "Your Personal Singing Teacher"

    # Selects the free trial plan.
    def select_monthly_plan(self):
        self.wait_and_click(*self.MONTHLY_PLAN_FIELD)

    # Click on Pay button
    def click_pay_button(self):
        self.wait_and_click(*self.PAY_BUTTON)
