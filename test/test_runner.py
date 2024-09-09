import pytest
from page_objects.test_login import LoginLogout
from page_objects.test_my_info import MyInfo


@pytest.mark.usefixtures("setup")
class Test:

    def test_run(self):
        login_logout = LoginLogout(self.driver)
        user_management = login_logout.login()
        '''user_management.add_user_credentials()
        leave_page = user_management.delete_user_from_users_list()
        Recruitment_page = leave_page.input_leave_details()
        my_info_page = Recruitment_page.input_recruitment_details()'''
        my_info_page = MyInfo(self.driver)
        my_info_page.input_personal_details()
        my_info_page.add_attachment()
        login_logout.logout()
