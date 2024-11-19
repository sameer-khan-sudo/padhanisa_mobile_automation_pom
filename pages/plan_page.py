
from appium.webdriver.common.appiumby import AppiumBy
from datetime import datetime, timedelta


from pages.base_class import BaseClass


class PlanPage(BaseClass):

    # Helper function to get the expiry date formatted string
    def get_formatted_expiry_date(days=14):
        current_date = datetime.now()
        expiry_date = current_date + timedelta(days=days)
        return expiry_date.strftime("%d %B %Y")

    formatted_expiry_date = get_formatted_expiry_date()
    print("Calculated expiry date: ", formatted_expiry_date)

    # Locators
    FREE_TRIAL_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Free Trial"]')
    FREE_TRIAL_NUDGE = (AppiumBy.XPATH, '//android.view.View[@content-desc="Start Trial"]')
    FREE_TRIAL_FIELD_LOCATOR = '//android.view.View[contains(@content-desc,"Trial Plan")]'
    CONTINUE_BUTTON_LOCATOR = '//android.widget.ImageView[@content-desc="Continue"]'

    GO_PREMIUM_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Go Premium"]')
    CHOOSE_YOUR_PLAN_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Choose Your Plan"]')
    FREE_TRIAL_BENEFITS_LOCATOR = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Enjoy All Premium Benefits With\n14 Days FREE Trial"]'
    )
    PREMIUM_BENEFITS_LOCATOR = (
    AppiumBy.XPATH, '//android.view.View[@content-desc="Get Access To All Premium Benefits"]')

    YOUR_TEXT_LOCATOR = (AppiumBy.XPATH,'android.view.View[@content-desc="Your"]')
    DAYS_FREE_PREMIUM_LOCATOR = (AppiumBy.XPATH,'android.view.View[@content-desc="14 Days Free Premium"]')
    IS_NOW_ACTIVE_LOCATOR = (AppiumBy.XPATH,'android.view.View[@content-desc="is now active."]')

    TRIAL_EXPIRY_MESSAGE_LOCATOR = (AppiumBy.XPATH,f'//android.view.View[@content-desc="Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}"]')

    # Expected Text
    EXPECTED_GO_PREMIUM_HEADER_TEXT = 'Go Premium'
    EXPECTED_CHOOSE_YOUR_PLAN_HEADER_TEXT = 'Choose Your Plan'
    EXPECTED_FREE_TRIAL_BENEFITS_TEXT = 'Enjoy All Premium Benefits With\n14 Days FREE Trial'

    EXPECTED_YOUR_TEXT = 'Your'
    EXPECTED_DAYS_FREE_PREMIUM_TEXT = '14 Days Free Premium'
    EXPECTED_IS_NOW_ACTIVE_TEXT = 'is now active.'
    EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT = f"Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}"








