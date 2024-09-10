import time
import allure
from allure_commons.types import AttachmentType

from locators.logger import TestLogger
from page_objects.test_user_management import User
from utilities.excel_data_reader import data_reader
from utilities.generic_methods import Generic


class LoginLogout(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = data_reader("login_credentials")
        # self.test_logger = TestLogger(self.driver)

    def login(self, request):
        self.send_keys_to_element(self.user_name, self.data[0])
        self.send_keys_to_element(self.password, self.data[1])
        with allure.step("login to the application"):
            self.click_on_element(self.login_btn)
            time.sleep(2)
            # self.test_logger.attach_screenshot_to_report(request, self.data[2][1])
            allure.attach(self.driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
        user_management = User(self.driver)
        return user_management

    def logout(self):
        self.click_on_element(self.user_profile_btn)
        self.click_on_element(self.logout_btn)


