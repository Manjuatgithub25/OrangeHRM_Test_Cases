import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.generic_methods import Generic


class MyInfo(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.w = WebDriverWait(driver, 10)
        self.a = ActionChains(driver)

    def click_on_my_info(self):
        self.click_on_element(self.my_info)

    def input_personal_details(self, personal_first_name, personal_last_name, emp_id, driver_license_id,
                               licenseExpiryDate, info_year, info_month, info_date, expected_my_info_success_msg):
        form = self.driver.find_element(*self.switch_to_form)
        time.sleep(2)
        self.clear_and_send(self.first_name, personal_first_name)
        self.clear_and_send(self.last_name, personal_last_name)
        self.clear_and_send(self.employee_id, emp_id)
        self.clear_and_send(self.driver_license, driver_license_id)
        self.clear_and_send(self.license_expiry_date, licenseExpiryDate)
        NationalityBtn = form.find_element(*self.nationality)
        NationalityBtn.click()
        nationality_options = form.find_element(*self.nationality_option)
        nationality_options.click()
        MaritalStatus = form.find_element(*self.marital_status)
        MaritalStatus.click()
        MaritalStatusOption = form.find_element(*self.marital_status_option)
        MaritalStatusOption.click()
        DOB = form.find_element(*self.dob)
        DOB.click()
        self.calender(info_year, info_month, info_date)
        gender = form.find_element(*self.gender)
        self.a.move_to_element(gender).click().perform()
        self.click_on_element(self.save_btn)
        actual_myinfo_success_msg = self.wait_until_presence_element_located(self.Saved_msg).text
        print(actual_myinfo_success_msg)
        time.sleep(1)
        assert expected_my_info_success_msg == actual_myinfo_success_msg.strip(), "Adding my_info details is failed"





