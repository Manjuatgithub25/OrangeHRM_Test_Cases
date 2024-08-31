import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions

from page_objects.test_leave import Leave
from utilities.generic_methods import Generic


class User(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def click_admin(self):
        self.click_on_element(self.admin)

    # The below function verifies if the current page is in the system user page or not. If it's not in the system
    # user page it'll be directed to the expected page.
    def system_user_verification(self, expected_url):
        self.url_verification(expected_url)

    def add_user_btn(self):
        self.click_on_element(self.add_btn)

    def add_user_credentials(self, emp_name, user_input, input_pw, input_confirm_pw, added_user_step_name,
                             added_user_screenshot_name, expected_add_user_success_msg):
        form = self.wait_until_visibility_element_located(self.switch_to_form)
        UserRoleDropdown = form.find_element(*self.user_role_dropdown)
        UserRoleDropdown.click()
        ClickAdminOption = form.find_element(*self.click_admin_option)
        ClickAdminOption.click()
        StatusDropdown = form.find_element(*self.status_dropdown)
        StatusDropdown.click()
        ClickEnabledOPtion = form.find_element(*self.click_enabled_option)
        ClickEnabledOPtion.click()
        self.send_keys_to_element(self.employee_name, emp_name)
        self.click_on_element(self.employee_option)
        self.send_keys_to_element(self.username, user_input)
        self.send_keys_to_element(self.pw, input_pw)
        self.send_keys_to_element(self.confirm_pw, input_confirm_pw)
        self.click_on_element(self.save_btn)
        actual_success_msg = self.driver.find_element(*self.Saved_msg).text
        assert expected_add_user_success_msg == actual_success_msg.strip(), "Adding user process is failed"
        waited = self.wait_until_visibility_element_located(self.user_name_list)
        names_list = waited.find_elements(*self.user_name_list)
        for names in names_list:
            if user_input == names.text:
                self.driver.execute_script("window.scrollBy(0, 300)")
                self.take_screenshot_attach_toAllure(added_user_step_name, added_user_screenshot_name)

    def delete_user_from_users_list(self, user_input, expected_delete_user_success_msg):
        self.wait_until_visibility_element_located(self.user_name_list)
        names_list = self.driver.find_elements(*self.user_name_list)
        for names in names_list:
            if user_input == names.text:
                names.find_element(*self.delete_user).click()
                self.wait_until_visibility_element_located(self.delete_user_btn)
                self.click_on_element(self.delete_user_btn)
                actual_deleted_msg = self.driver.find_element(*self.delete_msg).text
                assert expected_delete_user_success_msg == actual_deleted_msg.strip(), "The deletion of user is failed"
                break
        leave_page = Leave(self.driver)
        return leave_page


