
from appium.webdriver.common.appiumby import AppiumBy
from datetime import datetime, timedelta


from pages.base_class import BaseClass
from utils.helpers import get_formatted_expiry_date


class PlanPage(BaseClass):

    formatted_expiry_date = get_formatted_expiry_date(13)
    print("Calculated expiry date: ", formatted_expiry_date)

    # Locators
    FREE_TRIAL_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Free Trial"]')
    FREE_TRIAL_NUDGE = (AppiumBy.XPATH, '//android.view.View[@content-desc="Start Trial"]')
    FREE_TRIAL_FIELD_LOCATOR = '//android.view.View[contains(@content-desc,"Trial Plan")]'
    CONTINUE_BUTTON_LOCATOR = '//android.widget.ImageView[@content-desc="Continue"]'
    START_LEARNING_BUTTON_LOCATOR = '//android.widget.ImageView[@content-desc="Start Learning"]'

    GO_PREMIUM_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Go Premium"]')
    CHOOSE_YOUR_PLAN_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Choose Your Plan"]')
    FREE_TRIAL_BENEFITS_LOCATOR = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Enjoy All Premium Benefits With\n14 Days FREE Trial"]'
    )
    PREMIUM_BENEFITS_LOCATOR = (
    AppiumBy.XPATH, '//android.view.View[@content-desc="Get Access To All Premium Benefits"]')

    FREE_TRIAL_ACTIVATED_HEADER_LOCATOR = (AppiumBy.XPATH,'//android.view.View[@content-desc="Free Trial Activated"]')
    YOUR_TEXT_LOCATOR = (AppiumBy.XPATH,'android.view.View[@content-desc="Your"]')
    DAYS_FREE_PREMIUM_LOCATOR = (AppiumBy.XPATH,'android.view.View[@content-desc="14 Days Free Premium"]')
    IS_NOW_ACTIVE_LOCATOR = (AppiumBy.XPATH,'android.view.View[@content-desc="is now active."]')

    TRIAL_EXPIRY_MESSAGE_LOCATOR = (AppiumBy.XPATH,f'//android.view.View[@content-desc="Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}"]')

    # Expected Text
    EXPECTED_GO_PREMIUM_HEADER_TEXT = 'Go Premium'
    EXPECTED_CHOOSE_YOUR_PLAN_HEADER_TEXT = 'Choose Your Plan'
    EXPECTED_FREE_TRIAL_BENEFITS_TEXT = 'Enjoy All Premium Benefits With\n14 Days FREE Trial'

    EXPECTED_FREE_TRIAL_TEXT = 'Free Trial Activated'
    EXPECTED_YOUR_TEXT = 'Your'
    EXPECTED_DAYS_FREE_PREMIUM_TEXT = '14 Days Free Premium'
    EXPECTED_IS_NOW_ACTIVE_TEXT = 'is now active.'
    EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT = f"Enjoy unlimited access to all Premium benefits. Plan expiry: {formatted_expiry_date}"

    # Extract expiry date from the message
    @staticmethod
    def extract_and_compare_expiry_date():
        extracted_text = PlanPage.EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT.split(' ')
        last_index = ' '.join(extracted_text[-3:])  # Extract the last three words (date)
        print("Extracted expiry date from message: ", last_index)

        # Compare the extracted date with the calculated expiry date
        # if last_index == PlanPage.formatted_expiry_date:
        #     print("Match found: The extracted date matches the current date + 14 days.")
        # else:
        #     print(f"Mismatch: Expected '{PlanPage.formatted_expiry_date}', but found '{last_index}'.")









