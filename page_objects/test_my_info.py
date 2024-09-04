import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from utilities.excel_data_reader import excel_to_dictionary
from utilities.generic_methods import Generic


class MyInfo(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.w = WebDriverWait(driver, 10)
        self.a = ActionChains(driver)
        self.data = excel_to_dictionary("my_info")
        print(self.data)

    def click_on_my_info(self):
        self.click_on_element(self.my_info)

    def input_personal_details(self):
        form = self.driver.find_element(*self.switch_to_form)
        time.sleep(2)
        self.clear_and_send(self.first_name, self.data['personal_first_name'])
        self.clear_and_send(self.last_name, self.data['personal_last_name'])
        self.clear_and_send(self.employee_id, self.data['emp_id'])
        self.clear_and_send(self.driver_license, self.data['driver_license_id'])
        self.click_on_element(self.license_expiry_date)
        self.calender(self.data['licenseExpiryYear'], self.data['licenseExpiryMonth'], self.data['licenseExpiryDate'])
        self.click_on_element(self.calender_close_btn)
        NationalityBtn = form.find_element(*self.nationality)
        self.a.move_to_element(NationalityBtn).click().perform()
        nationality_options = form.find_element(*self.nationality_option)
        nationality_options.click()
        MaritalStatus = form.find_element(*self.marital_status)
        MaritalStatus.click()
        MaritalStatusOption = form.find_element(*self.marital_status_option)
        MaritalStatusOption.click()
        DOB = form.find_element(*self.dob)
        DOB.click()
        self.calender(self.data['info_year'], self.data['info_month'], self.data['info_date'])
        gender = form.find_element(*self.gender)
        self.a.move_to_element(gender).click().perform()
        self.click_on_element(self.save_btn)
        actual_myinfo_success_msg = self.wait_until_presence_element_located(self.Saved_msg).text
        print(actual_myinfo_success_msg)
        time.sleep(1)
        assert self.data['expected_my_info_success_msg'] == actual_myinfo_success_msg.strip(), "Adding my_info details is failed"





