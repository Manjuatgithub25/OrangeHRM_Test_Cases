import time
import pytest
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

    # @pytest.xfail
    def input_personal_details(self):
        self.click_on_element(self.my_info)
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


    @pytest.mark.xfail
    def add_attachment(self):
        self.click_on_element(self.my_info)
        self.click_on_element(self.attachments)
        self.send_keys_to_element(self.file_input, self.data['file_input'])
        self.driver.execute_script("window.scrollBy(0, 500);")
        file_list = self.driver.find_elements(*self.attachments_list)
        for attachment in file_list:
            if self.data['attachment'] == attachment.text:
                # self.driver.execute_script("window.scrollBy(0,260);")
                self.take_screenshot_attach_toAllure(self.data['added_file_step_name'],
                                                     self.data['added_file_screenshot_name'])
                download = attachment.find_element(*self.download_file)
                self.a.click(download).perform()
                time.sleep(4)
                break
