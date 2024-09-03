import pytest

from page_objects.test_login import LoginLogout
from page_objects.test_my_info import MyInfo
from page_objects.test_recruitment import Recruitment
from utilities.data_page import Data


@pytest.mark.usefixtures("setup")
class Test(Data):

    def test_run(self):
        login_logout = LoginLogout(self.driver)
        user_management = login_logout.login()
        Recruitment_page = Recruitment(self.driver)
        '''user_management.click_admin()
        user_management.system_user_verification(self.system_users)
        user_management.add_user_btn()
        user_management.add_user_credentials(self.emp_name, self.user_input, self.input_pw, self.input_confirm_pw,
                                             self.added_user_step_name, self.added_user_screenshot_name,
                                             self.expected_add_user_success_msg)
        leave_page = user_management.delete_user_from_users_list(self.user_input, self.expected_delete_user_success_msg)
        leave_page.click_on_leave()
        Recruitment_page = leave_page.input_leave_details(self.Year, self.Month, self.Date, self.year, self.month, self.date,
                                                          self.expected_leave_successful_msg)'''
        Recruitment_page.click_on_recruitment()
        Recruitment_page.input_recruitment_details(self.first_name, self.last_name, self.email,
                                                   self.contact_num,
                                                   self.file_path, self.input_keywords,
                                                   self.recruitment_year,
                                                   self.recruitment_month, self.recruitment_date,
                                                   self.expected_recruitment_successful_msg,
                                                   self.candidate,
                                                   self.added_recruitment_step_name,
                                                   self.added_recruitment_screenshot_name)
        '''my_info_page.click_on_my_info()
        my_info_page.input_personal_details(self.personal_first_name, self.personal_last_name, self.emp_id,
                                            self.driver_license_id, self.licenseExpiryDate, self.info_year,
                                            self.info_month, self.info_date, self.expected_my_info_success_msg)'''

        # login_logout.logout()
