import time

import allure
from allure_commons.types import AttachmentType

from page_objects.test_user_management import User
from utilities.excel_data_reader import data_reader
from utilities.generic_methods import Generic


class LoginLogout(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        data = data_reader("login_credentials")
        self.send_keys_to_element(self.user_name, data[0])
        self.send_keys_to_element(self.password, data[1])
        with allure.step("login to the application"):
            self.click_on_element(self.login_btn)
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
        user_management = User(self.driver)
        return user_management

    def logout(self):
        self.click_on_element(self.user_profile_btn)
        self.click_on_element(self.logout_btn)


