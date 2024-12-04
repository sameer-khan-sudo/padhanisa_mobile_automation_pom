import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_class import BaseClass
from utils.helpers import get_formatted_expiry_date


class PlanPage(BaseClass):
    free_trial_expiry_date = get_formatted_expiry_date(14)
    print("Calculated expiry date: ", free_trial_expiry_date)

    monthly_plan_expiry_date = get_formatted_expiry_date(30)
    print("Calculated expiry date: ", monthly_plan_expiry_date)

    # Button Locators
    FREE_TRIAL_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Free Trial"]')
    CONTINUE_BUTTON_LOCATOR = '//android.widget.ImageView[@content-desc="Continue"]'
    PAY_BUTTON_LOCATOR = '//android.widget.ImageView[contains(@content-desc,"Proceed to Pay")]'
    START_LEARNING_BUTTON_LOCATOR = 'new UiSelector().description("Start Learning")'

    # Other Locators
    FREE_TRIAL_NUDGE = (AppiumBy.XPATH, '//android.view.View[@content-desc="Start Trial"]')
    FREE_TRIAL_FIELD_LOCATOR = '//android.view.View[contains(@content-desc,"Trial Plan")]'
    MONTHLY_PLAN_FIELD_LOCATOR = '//android.view.View[contains(@content-desc,"Monthly")]'
    YEARLY_PLAN_FIELD_LOCATOR = '//android.view.View[contains(@content-desc,"Yearly")]'
    GO_PREMIUM_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Go Premium"]')
    CHOOSE_YOUR_PLAN_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Choose Your Plan"]')
    FREE_TRIAL_BENEFITS_LOCATOR = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Enjoy All Premium Benefits With\n14 Days FREE Trial"]'
    )
    PREMIUM_BENEFITS_LOCATOR = (
        AppiumBy.XPATH, '//android.view.View[@content-desc="Get Access To All Premium Benefits"]'
    )
    FREE_TRIAL_ACTIVATED_HEADER_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Free Trial Activated"]')
    YOUR_TEXT_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your"]')
    DAYS_FREE_PREMIUM_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="14 Days Free Premium"]')
    IS_NOW_ACTIVE_LOCATOR = (AppiumBy.XPATH, '//android.view.View[@content-desc="is now active."]')
    TRIAL_EXPIRY_MESSAGE_LOCATOR = (AppiumBy.XPATH,
                                    f'//android.view.View[@content-desc="Enjoy unlimited access to all Premium benefits. Plan expiry: {free_trial_expiry_date}"]')
    PREMIUM_TAG_LOCATOR = '//android.widget.ImageView[@content-desc="Premium"]'

    # Plan Success message locator
    MONTHLY_SUCCESS_MESSAGE_LOCATOR = f'''//android.widget.ImageView[@content-desc="Plan Activated\nYour Premium plan is now active. Enjoy unlimited access to all Premium benefits.\nPlan expiry: {monthly_plan_expiry_date}"]'''

    # Expected Text
    EXPECTED_GO_PREMIUM_HEADER_TEXT = 'Go Premium'
    EXPECTED_CHOOSE_YOUR_PLAN_HEADER_TEXT = 'Choose Your Plan'
    EXPECTED_FREE_TRIAL_BENEFITS_TEXT = 'Enjoy All Premium Benefits With\n14 Days FREE Trial'
    EXPECTED_PREMIUM_BENEFITS_TEXT = "Get Access To All Premium Benefits"

    EXPECTED_FREE_TRIAL_TEXT = 'Free Trial Activated'
    EXPECTED_YOUR_TEXT = 'Your'
    EXPECTED_DAYS_FREE_PREMIUM_TEXT = '14 Days Free Premium'
    EXPECTED_IS_NOW_ACTIVE_TEXT = 'is now active.'
    EXPECTED_TRIAL_EXPIRY_MESSAGE_TEXT = f"Enjoy unlimited access to all Premium benefits. Plan expiry: {free_trial_expiry_date}"
    EXPECTED_MONTHLY_SUCCESS_MESSAGE_TEXT = f"Plan Activated\nYour Premium plan is now active. Enjoy unlimited access to all Premium benefits.\nPlan expiry: {monthly_plan_expiry_date}"

    # Click on 'View More' button
    def view_more_click(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(431, 1201)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    # Click on 'Start Learning' button
    def click_start_learning(self):
        try:
            # Wait for the Start Learning button to be visible before clicking
            start_learning_button = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.START_LEARNING_BUTTON_LOCATOR))
            )
            start_learning_button.click()
            logging.info("Clicked on Start Learning button.")
        except Exception as e:
            logging.error(f"Error while clicking on Start Learning button: {e}")
            raise  # Re-raise the exception to ensure the test fails appropriately
