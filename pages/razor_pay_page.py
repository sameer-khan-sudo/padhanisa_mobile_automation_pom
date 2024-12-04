from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import time

from conftest import driver
from pages.base_class import BaseClass

class RazorPayPage(BaseClass):
    # Locators
    BRAND_NAME_LOCATOR = '//android.widget.TextView[@text="Saregama India Ltd."]'
    UPI_FIELD_LOCATOR = '//android.view.View[@text="UPI ..."]'
    UPI_TEXT_FIELD_LOCATOR = '//android.widget.EditText'
    PAY_NOW_BUTTON_LOCATOR = '//android.widget.Button[@text="Pay Now"]'

    def test_upi_payment(self, driver):
        try:
            # Initialize WebDriverWait with the driver and timeout
            wait = WebDriverWait(driver, 30)

            # Wait until the brand name element is visible
            ele = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.BRAND_NAME_LOCATOR)))

            # Get the Brand name
            brand_name = ele.get_attribute("text")
            print(f'\nBrand Name: {brand_name}')
            assert brand_name == 'Saregama India Ltd.', f"Expected brand name to be 'Saregama India Ltd.', but got {brand_name}"

            # Start the UPI payment process
            self.wait_and_click(AppiumBy.XPATH, self.UPI_FIELD_LOCATOR)  # Select UPI payment type

            # Enter UPI ID
            upi_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.UPI_TEXT_FIELD_LOCATOR)))
            upi_field.send_keys('success@razorpay')  # Replace with your UPI ID

            # Click on 'Pay Now' button
            self.wait_and_click(AppiumBy.XPATH, self.PAY_NOW_BUTTON_LOCATOR)
            logging.info("Clicked on Pay Now button.")
            time.sleep(1)

        except Exception as e:
            logging.error(f"Error while making payment: {e}")
            raise  # Re-raise the exception to ensure the test fails appropriately
