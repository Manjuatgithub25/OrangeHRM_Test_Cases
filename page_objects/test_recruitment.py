import time

from selenium.webdriver import ActionChains

from page_objects.test_my_info import MyInfo
from utilities.excel_data_reader import excel_to_dictionary
from utilities.generic_methods import Generic


class Recruitment(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.a = ActionChains(driver)
        self.data = excel_to_dictionary("recruitment")

    def click_on_recruitment(self):
        self.click_on_element(self.click_recruitment)

    def input_recruitment_details(self):
        self.click_on_element(self.add_btn)
        form = self.driver.find_element(*self.switch_to_form)
        self.send_keys_to_element(self.first_name, self.data['first_name'])
        self.send_keys_to_element(self.last_name, self.data['last_name'])
        ClickVacancy = form.find_element(*self.drop_down)
        ClickVacancy.click()
        Choosevacancy = form.find_element(*self.choose_vacancy)
        Choosevacancy.click()
        self.send_keys_to_element(self.Email, str(self.data['email']))
        self.send_keys_to_element(self.contact_number, str(self.data['contact_num']))
        self.send_keys_to_element(self.file_input, str(self.data['file_path']))
        EnterKeywords = form.find_element(*self.keywords)
        EnterKeywords.send_keys(self.data['input_keywords'])
        DateOfApplication = form.find_element(*self.date_of_application)
        DateOfApplication.click()
        self.calender(str(self.data['recruitment_year']), self.data['recruitment_month'], str(self.data['recruitment_date']))
        self.click_on_element(self.calender_close_btn)
        self.click_on_element(self.consent_btn)
        self.click_on_element(self.save_btn)
        actual_msg = form.find_element(*self.leave_successful_msg).text
        time.sleep(1)
        # assert actual_msg == expected_recruitment_successful_msg, "Adding recruitment is failed"
        candidates = form.find_element(*self.click_candidates)
        candidates.click()
        waited = self.wait_until_visibility_element_located(self.candidate_list)
        names_list = waited.find_elements(*self.candidate_list)
        for names in names_list:
            if self.data['candidate'] == names.text:
                # assert candidate == names.text, "candidate name and names in records doesn't match"
                self.driver.execute_script("arguments[0].scrollIntoView(true);", names)
                self.take_screenshot_attach_toAllure(self.data['added_recruitment_step_name'], self.data['added_recruitment_screenshot_name'])
                time.sleep(3)
                download = names.find_element(*self.download_resume)
                self.driver.execute_script("window.scrollBy(0, 100);")
                self.a.click(download).perform()
                time.sleep(7)
                break
        my_info_page = MyInfo(self.driver)
        return my_info_page






