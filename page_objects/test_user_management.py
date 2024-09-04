import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions

from page_objects.test_leave import Leave
from utilities.excel_data_reader import excel_to_dictionary
from utilities.generic_methods import Generic


class User(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = excel_to_dictionary("user_management")

    def click_admin(self):
        self.click_on_element(self.admin)

    def add_user_btn(self):
        self.click_on_element(self.add_btn)

    def add_user_credentials(self):
        form = self.wait_until_visibility_element_located(self.switch_to_form)
        UserRoleDropdown = form.find_element(*self.user_role_dropdown)
        UserRoleDropdown.click()
        ClickAdminOption = form.find_element(*self.click_admin_option)
        ClickAdminOption.click()
        StatusDropdown = form.find_element(*self.status_dropdown)
        StatusDropdown.click()
        ClickEnabledOPtion = form.find_element(*self.click_enabled_option)
        ClickEnabledOPtion.click()
        self.send_keys_to_element(self.employee_name, self.data['emp_name'])
        self.click_on_element(self.employee_option)
        self.send_keys_to_element(self.username, self.data['user_input'])
        self.send_keys_to_element(self.pw, self.data['input_pw'])
        self.send_keys_to_element(self.confirm_pw, self.data['input_confirm_pw'])
        self.click_on_element(self.save_btn)
        actual_success_msg = self.driver.find_element(*self.Saved_msg).text
        # assert expected_add_user_success_msg == actual_success_msg.strip(), "Adding user process is failed"
        waited = self.wait_until_visibility_element_located(self.user_name_list)
        names_list = waited.find_elements(*self.user_name_list)
        for names in names_list:
            if self.data['user_input'] == names.text:
                self.driver.execute_script("window.scrollBy(0, 300)")
                self.take_screenshot_attach_toAllure(self.data['added_user_step_name'], self.data['added_user_screenshot_name'])
                break

    def delete_user_from_users_list(self):
        self.wait_until_visibility_element_located(self.user_name_list)
        names_list = self.driver.find_elements(*self.user_name_list)
        for names in names_list:
            if self.data['user_input'] == names.text:
                names.find_element(*self.delete_user).click()
                self.wait_until_visibility_element_located(self.delete_user_btn)
                self.click_on_element(self.delete_user_btn)
                # actual_deleted_msg = self.driver.find_element(*self.delete_msg).text assert self.data[
                # 'expected_delete_user_success_msg'] == actual_deleted_msg.strip(), "The deletion of user is failed"
                break
        leave_page = Leave(self.driver)
        return leave_page


