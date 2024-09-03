import pytest
from page_objects.test_login import LoginLogout


@pytest.mark.usefixtures("setup")
class Test:

    def test_run(self):
        login_logout = LoginLogout(self.driver)
        user_management = login_logout.login()
        user_management.click_admin()
        user_management.add_user_btn()
        user_management.add_user_credentials()
        leave_page = user_management.delete_user_from_users_list()
        leave_page.click_on_leave()
        Recruitment_page = leave_page.input_leave_details()
        Recruitment_page.click_on_recruitment()
        my_info_page = Recruitment_page.input_recruitment_details()
        my_info_page.click_on_my_info()
        my_info_page.input_personal_details()
        login_logout.logout()
