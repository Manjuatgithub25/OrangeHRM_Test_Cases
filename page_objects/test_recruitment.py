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
        self.logger = self.setup_logger()
        self.data = excel_to_dictionary("recruitment")

    def input_recruitment_details(self):
        try:
            self.click_on_element(self.click_recruitment)
            self.click_on_element(self.add_btn)
            form = self.driver.find_element(*self.switch_to_form)
            self.send_keys_to_element(self.first_name, self.data['first_name'])
            self.send_keys_to_element(self.last_name, self.data['last_name'])
            ClickVacancy = form.find_element(*self.drop_down)
            ClickVacancy.click()
            Choosevacancy = form.find_element(*self.choose_vacancy)
            Choosevacancy.click()
            self.send_keys_to_element(self.Email, self.data['email'])
            self.send_keys_to_element(self.contact_number, self.data['contact_num'])
            self.send_keys_to_element(self.file_input, self.data['file_path'])
            EnterKeywords = form.find_element(*self.keywords)
            EnterKeywords.send_keys(self.data['input_keywords'])
            DateOfApplication = form.find_element(*self.date_of_application)
            DateOfApplication.click()
            self.calender(self.data['recruitment_year'], self.data['recruitment_month'], self.data['recruitment_date'])
            self.click_on_element(self.calender_close_btn)
            self.click_on_element(self.consent_btn)
            self.click_on_element(self.save_btn)
            self.logger.info("Recruitment details are saved")
            self.click_on_element(self.click_candidates)
            names_list = self.driver.find_elements(*self.candidate_list)
            for names in names_list:
                if self.data['candidate'] == names.text:
                    self.driver.execute_script("window.scrollBy(0,300);")
                    self.take_screenshot_attach_toAllure(self.data['added_recruitment_step_name'], self.data['added_recruitment_screenshot_name'])
                    download = names.find_element(*self.download_resume)
                    self.a.move_to_element(download).click(download).perform()
                    self.logger.info("Resume successfully downloaded")
                    break

        except Exception as e:
            print(e)

        finally:
            my_info_page = MyInfo(self.driver)
            return my_info_page






