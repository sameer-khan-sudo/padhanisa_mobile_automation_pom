from appium.webdriver.common.appiumby import AppiumBy
from datetime import datetime, timedelta
from pages.base_class import BaseClass


class FreeTrialPage(BaseClass):
    CONTINUE_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Continue"]')
    SUCCESS_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Free Trial Activated"]')
    START_LEARNING_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Start Learning"]')
    HOME_SCREEN_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your Personal Singing Teacher"]')

    def click_continue(self):
        self.click_element(*self.CONTINUE_BUTTON)

    def get_formatted_expiry_date(self, days=14):
        current_date = datetime.now()
        expiry_date = current_date + timedelta(days=days)
        return expiry_date.strftime("%d %B %Y")

    def verify_free_trial_activation(self):
        formatted_expiry_date = self.get_formatted_expiry_date()
        expiry_message = f'Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}'
        expiry_message_locator = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{expiry_message}"]')

        self.verify_text_on_screen(self.SUCCESS_HEADER, "Free Trial Activated")
        self.verify_text_on_screen(expiry_message_locator, expiry_message)

    def click_start_learning(self):
        self.click_element(*self.START_LEARNING_BUTTON)

    def verify_home_screen(self):
        self.verify_text_on_screen(self.HOME_SCREEN_HEADER, "Your Personal Singing Teacher")
