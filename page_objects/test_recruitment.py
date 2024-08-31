import time

from page_objects.test_my_info import MyInfo
from utilities.generic_methods import Generic


class Recruitment(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_recruitment(self):
        self.click_on_element(self.click_recruitment)

    def input_recruitment_details(self, first_name, last_name, email, contact_num, file_path, input_keywords,
                                  recruitment_year, recruitment_month, recruitment_date,
                                  expected_recruitment_successful_msg, candidate, added_recruitment_step_name,
                                  added_recruitment_screenshot_name):
        self.click_on_element(self.add_btn)
        form = self.driver.find_element(*self.switch_to_form)
        self.send_keys_to_element(self.first_name, first_name)
        self.send_keys_to_element(self.last_name, last_name)
        ClickVacancy = form.find_element(*self.drop_down)
        ClickVacancy.click()
        Choosevacancy = form.find_element(*self.choose_vacancy)
        Choosevacancy.click()
        self.send_keys_to_element(self.Email, email)
        self.send_keys_to_element(self.contact_number, contact_num)
        self.send_keys_to_element(self.file_input, file_path)
        EnterKeywords = form.find_element(*self.keywords)
        for words in input_keywords:
            EnterKeywords.send_keys(words)
        DateOfApplication = form.find_element(*self.date_of_application)
        DateOfApplication.click()
        self.calender(recruitment_year, recruitment_month, recruitment_date)
        self.click_on_element(self.calender_close_btn)
        self.click_on_element(self.consent_btn)
        self.click_on_element(self.save_btn)
        actual_msg = form.find_element(*self.leave_successful_msg).text
        time.sleep(1)
        assert actual_msg == expected_recruitment_successful_msg, "Adding recruitment is failed"
        waited = self.wait_until_visibility_element_located(self.candidate_list)
        names_list = waited.find_elements(*self.candidate_list)
        for names in names_list:
            if candidate == names.text:
                # self.driver.execute_script("window.scrollBy(0, 300)")
                assert candidate == names.text, "candidate name and names in records doesn't match"
                self.driver.execute_script("arguments[0].scrollIntoView(true);", names)
                self.take_screenshot_attach_toAllure(added_recruitment_step_name, added_recruitment_screenshot_name)
                names.click_on_element(self.download_resume)
                break
        my_info_page = MyInfo(self.driver)
        return my_info_page






