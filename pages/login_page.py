from appium.webdriver.common.appiumby import AppiumBy
from pages.base_class import BaseClass
from utils.utils import generate_random_mobile_number


class LoginPage(BaseClass):
    SIGN_IN_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Sign In"]')
    SKIP_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Skip"]')

    PHONE_NUMBER_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Get OTP')

    def click_sign_in(self):
        self.wait_and_click(*self.SIGN_IN_BUTTON)

    def click_skip(self):
        self.wait_and_click(*self.SKIP_BUTTON)

    def click_on_field(self):
        self.wait_and_click(*self.PHONE_NUMBER_FIELD)

    def enter_phone_number(self, phone_number):
        self.enter_text(self.PHONE_NUMBER_FIELD, str(phone_number))

    def click_get_otp(self):
        self.wait_and_click(*self.CONTINUE_BUTTON)

    def perform_login(self):
        phone_number = generate_random_mobile_number()  # Generate random mobile number
        self.enter_phone_number(phone_number)
        print(f'Generated Mobile Number: {phone_number}')  # Use the generated number
        self.click_get_otp()
