from turtledemo.clock import setup

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.devtools.v127.input_ import DragData

from conftest import driver
from pages.base_class import BaseClass


class RazorPayPage(BaseClass):
    # Locators
    BRAND_NAME_LOCATOR = '//android.widget.TextView[@text="Saregama India Ltd."]'
    UPI_FIELD_LOCATOR = '//android.view.View[@text="UPI ..."]'
    UPI_TEXT_FIELD_LOCATOR = '//android.widget.EditText'

    # CARD_FIELD_LOCATOR =
    # CARD_NUMBER_FIELD_LOCATOR =
    # EXPITY_FIELD_LOCATOR =
    # HOLDER_NAME_FIELD_LOCATOR =
    # CVV_FIELD_LOCATOR =
    #
    #
    # CHECK_BOX_LOCATOR =
    PAY_NOW_BUTTON_LOCATOR = '//android.widget.Button[@text="Pay Now"]'

    def upi_payment(self):
        self.wait_and_click(*self.UPI_FIELD_LOCATOR)
        self.enter_text(self.UPI_TEXT_FIELD_LOCATOR, 'success@razorpay')  # Replace with your UPI ID
        self.wait_and_click(*self.PAY_NOW_BUTTON_LOCATOR)