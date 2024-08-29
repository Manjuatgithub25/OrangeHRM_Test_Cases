import pytest

from page_objects.test_login import LoginLogout
from utilities.data_page import Data


@pytest.mark.usefixtures("setup")
class Test(Data):

    def test_run(self):

        login_logout = LoginLogout(self.driver)
        user_management = login_logout.login()
        user_management.click_admin()
        user_management.system_user_verification(self.system_users)
        user_management.add_user_btn()
        user_management.add_user_credentials(self.emp_name, self.user_input, self.input_pw, self.input_confirm_pw,
                                             self.added_user_step_name, self.added_user_screenshot_name,
                                             self.expected_add_user_success_msg)
        leave_page = user_management.delete_user_from_users_list(self.user_input, self.expected_delete_user_success_msg)
        leave_page.click_on_leave()
        leave_page.input_leave_details()


        # login_logout.logout()





