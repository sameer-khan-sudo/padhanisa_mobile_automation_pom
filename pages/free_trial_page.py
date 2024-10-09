from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class FreeTrialPage(BaseClass):
    CONTINUE_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Continue"]')
    SUCCESS_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Free Trial Activated"]')
    START_LEARNING_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Start Learning"]')
    HOME_SCREEN_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your Personal Singing Teacher"]')
    FREE_TRIAL_FIELD = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc,"Trial Plan")]')

    def click_continue(self):
        try:
            self.wait_and_click(*self.CONTINUE_BUTTON)
        except NoSuchElementException:
            print("Continue button not found")

    def get_formatted_expiry_date(self, days=14):
        current_date = datetime.now()
        expiry_date = current_date + timedelta(days=days)
        return expiry_date.strftime("%d %B %Y")

    def verify_free_trial_activation(self):
        try:
            formatted_expiry_date = self.get_formatted_expiry_date()
            expiry_message = f'Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}'
            expiry_message_locator = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{expiry_message}"]')

            self.verify_text_on_screen(self.SUCCESS_HEADER, "Free Trial Activated")
            self.verify_text_on_screen(expiry_message_locator, expiry_message)
        except TimeoutException:
            print("Free trial activation verification failed")

    def click_start_learning(self):
        try:
            self.wait_and_click(*self.START_LEARNING_BUTTON)
        except NoSuchElementException:
            print("Start Learning button not found")

    def verify_home_screen(self):
        try:
            self.verify_text_on_screen(self.HOME_SCREEN_HEADER, "Your Personal Singing Teacher")
        except TimeoutException:
            print("Home screen verification failed")

    def select_plan_type(self):
        try:
            self.wait_and_click(*self.FREE_TRIAL_FIELD)
        except NoSuchElementException:
            print("Free trial field not found")
