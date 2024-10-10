from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementNotVisibleException,
    WebDriverException
)

from utils.utils import get_formatted_expiry_date


class FreeTrialPage(BaseClass):
    SUCCESS_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Free Trial Activated"]')
    HOME_SCREEN_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your Personal Singing Teacher"]')
    FREE_TRIAL_FIELD = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc,"Trial Plan")]')
    CONTINUE_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Continue"]')

    # Selects the free trial plan.
    def select_trial_plan(self):
        try:
            self.wait_and_click(*self.FREE_TRIAL_FIELD)
        except (
                NoSuchElementException,
                TimeoutException,
                StaleElementReferenceException,
                ElementNotVisibleException,
                WebDriverException) as e:
            print(f"Error while selecting free trial plan: {str(e)}")

    # Clicks the Continue button.
    def click_continue(self):
        try:
            self.wait_and_click(*self.CONTINUE_BUTTON)
        except (
                NoSuchElementException,
                TimeoutException,
                StaleElementReferenceException,
                ElementNotVisibleException,
                WebDriverException) as e:
            print(f"Error while clicking on Continue button: {str(e)}")

    # Verifies free trial activation by message and expiry date
    def verify_free_trial_activation(self):
        try:
            # Get and format the expiry date
            formatted_expiry_date = get_formatted_expiry_date()

            expiry_message = f'Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}'
            expiry_message_locator = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{expiry_message}"]')

            self.verify_text_on_screen(self.SUCCESS_HEADER, "Free Trial Activated")
            self.verify_text_on_screen(expiry_message_locator, expiry_message)

            expiry_message_element = self.driver.find_element(*expiry_message_locator)
            content_desc = expiry_message_element.get_attribute('content-desc')
            print(f"Success Message: {content_desc}")

        except (
                NoSuchElementException,
                TimeoutException,
                StaleElementReferenceException,
                WebDriverException) as e:
            print(f"Error while verifying free trial activation: {str(e)}")

    # Verifies that the user is redirected to the home screen after trial activation.
    def verify_home_screen(self):
        try:
            self.verify_text_on_screen(self.HOME_SCREEN_HEADER, "Your Personal Singing Teacher")
        except (
                NoSuchElementException,
                TimeoutException,
                StaleElementReferenceException,
                WebDriverException) as e:
            print(f"Error while verifying home screen: {str(e)}")
