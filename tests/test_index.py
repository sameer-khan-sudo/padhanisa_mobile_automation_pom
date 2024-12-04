# import logging
# import time
#
# import pytest
#
# from conftest import driver
# from pages.create_profile_page import CreateProfile
# from pages.login_page import LoginPage
# from pages.plan_page import PlanPage
# from pages.profile_page import ProfilePage
# from pages.razor_pay_page import RazorPayPage
# from utils.helpers import scroll_down
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Test Data
# # USER_TYPE = 'EXIST'
# USER_TYPE = 'EXIST'
#
# EXISTING_USER_PHONE = '6000000000'
# PROFILE_NAME = 'Deadpool'
#
# NEW_USER_FIRST_NAME = 'Anonymous'
# NEW_USER_VOICE_TYPE = 'Male'
# NEW_USER_AGE_GROUP = '16 - 25'
# NEW_USER_SKILL_LEVEL = 'I Am A Singer'
# UPI_ID = 'success@razorpay'
#
# # Test cases for Monthly Plan workflow
# @pytest.mark.usefixtures("driver")
# class TestFreeTrial:
#
#     # Initialize the driver and page objects before each test.
#     @pytest.fixture(autouse=True)
#     def setup(self, driver):
#
#         self.driver = driver
#         self.login = LoginPage(driver)
#         self.create_user_profile = CreateProfile(driver)
#         self.plan = PlanPage(driver)
#         self.profile = ProfilePage(driver)
#         self.razorpay = RazorPayPage(driver)
#         self.get_initial = None  # Initialize as a class attribute
#
#     # Perform login and profile creation for new user
#     @pytest.mark.skipif(USER_TYPE != 'NEW', reason="Skipped because USER_TYPE is not 'NEW'")
#     def test_login_and_create_user_profile(self):
#         try:
#             logging.info("Starting login process...")
#             self.login.click_sign_in()
#             self.login.perform_login()
#             logging.info("Login successful.")
#
#             # Create User Profile
#             self.create_user_profile.enter_first_name(NEW_USER_FIRST_NAME)
#             logging.info(f"Entered first name: {NEW_USER_FIRST_NAME}")
#
#             self.create_user_profile.select_voice_type(NEW_USER_VOICE_TYPE)
#             logging.info(f"Voice type selected: {NEW_USER_VOICE_TYPE}")
#
#             scroll_down(self.driver)
#             logging.info("Scrolled down the page.")
#
#             self.create_user_profile.select_age(NEW_USER_AGE_GROUP)
#             logging.info(f"Age group selected: {NEW_USER_AGE_GROUP}")
#
#             self.create_user_profile.select_skill_level(NEW_USER_SKILL_LEVEL)
#             logging.info(f"Skill level selected: {NEW_USER_SKILL_LEVEL}")
#
#             self.create_user_profile.click_continue_button()
#             logging.info("Clicked on the Continue button.")
#
#         except Exception as e:
#             logging.error(f"An error occurred during profile creation: {e}")
#             pytest.fail(f"Test failed due to error: {e}")
#
#     # Login with an existing user
#     @pytest.mark.skipif(USER_TYPE != 'EXIST', reason="Skipped because USER_TYPE is not 'EXIST'")
#     def test_perform_exist_user_login(self):
#         """Login with an existing user and select a profile."""
#         try:
#             logging.info("Attempting login with an existing user.")
#             self.login.exist_user_login(EXISTING_USER_PHONE)
#             logging.info("Login with existing user successful.")
#
#             # Select profile
#             self.profile.select_profile(PROFILE_NAME)
#             logging.info("Profile selection successful.")
#             time.sleep(1)
#
#         except Exception as e:
#             pytest.fail(f"Login failed: {e}")
#
#     # Click on profile image to redirect to More menu
#     def test_redirect_more_menu(self):
#         """
#         Test case for redirecting to the 'More Menu'.
#         """
#


