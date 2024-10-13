from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass
from utils.utils import get_formatted_expiry_date


class FreeTrialPage(BaseClass):
    SUCCESS_SCREEN_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Free Trial Activated"]')
    HOME_SCREEN_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your Personal Singing Teacher"]')
    FREE_TRIAL_FIELD = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc,"Trial Plan")]')
    CONTINUE_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Continue"]')

    YOUR_TEXT_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Your")')
    DAYS_FREE_PREMIUM_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("14 Days Free Premium")')
    IS_NOW_ACTIVE_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("is now active.")')

    SUCCESS_SCREEN_HEADER_TEXT = 'Free Trial Activated'
    YOUR_TEXT = 'Your'
    DAYS_FREE_PREMIUM_TEXT = '14 Days Free Premium'
    IS_NOW_ACTIVE_TEXT = 'is now active.'
    HOME_SCREEN_HEADER_TEXT = "Your Personal Singing Teacher"

    # Selects the free trial plan.
    def select_trial_plan(self):
        self.wait_and_click(*self.FREE_TRIAL_FIELD)

    # Clicks the Continue button.
    def click_continue(self):
        self.wait_and_click(*self.CONTINUE_BUTTON)

    # Verifies free trial activation by message and expiry date
    def verify_free_trial_activation(self):
        # Get and format the expiry date
        formatted_expiry_date = get_formatted_expiry_date()

        expiry_message = f'Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}'
        expiry_message_locator = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{expiry_message}"]')

        # Verify other home screen texts
        text_locators = [
            self.SUCCESS_SCREEN_HEADER,
            self.YOUR_TEXT_LOCATOR,
            self.DAYS_FREE_PREMIUM_LOCATOR,
            self.IS_NOW_ACTIVE_LOCATOR,
            expiry_message_locator
        ]
        expected_texts = [
            self.SUCCESS_SCREEN_HEADER_TEXT,
            self.YOUR_TEXT,
            self.DAYS_FREE_PREMIUM_TEXT,
            self.IS_NOW_ACTIVE_TEXT,
            expiry_message
        ]

        # Verify all the text, message and expiry on the screen
        self.verify_text_on_screen(text_locators, expected_texts)

    def verify_screen_redirection(self, screen_type):
        if screen_type == 'Home':
            self.verify_text_on_screen(
                (AppiumBy.XPATH, '//android.view.View[@content-desc="Your Personal Singing Teacher"]'),
                'Your Personal Singing Teacher'
            )
            print("Home screen redirection verified successfully.")

        elif screen_type == 'My Plan':
            self.verify_text_on_screen(
                (AppiumBy.XPATH, '//android.view.View[@content-desc="My Plan"]'),
                'My Plan'
            )
            print("'My Plan' screen redirection verified successfully.")
