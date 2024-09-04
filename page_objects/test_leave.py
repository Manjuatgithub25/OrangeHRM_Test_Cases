import time

from selenium.webdriver.support.wait import WebDriverWait

from page_objects.test_recruitment import Recruitment
from utilities.excel_data_reader import excel_to_dictionary
from utilities.generic_methods import Generic


class Leave(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.w = WebDriverWait(driver, 10)
        self.data = excel_to_dictionary("leave")

    def click_on_leave(self):
        self.click_on_element(self.leave_btn)

    def input_leave_details(self):
        self.click_on_element(self.apply_btn)
        try:
            form = self.driver.find_element(*self.switch_to_form)
            Leave_type = form.find_element(*self.drop_down)
            Leave_type.click()
            Leave_Type_Option = form.find_element(*self.leave_type_option)
            Leave_Type_Option.click()
            FromDate = form.find_element(*self.from_date)
            FromDate.click()
            self.calender(str(self.data['Year']), self.data['Month'], str(self.data['Date']))
            time.sleep(1)
            ToDate = form.find_element(*self.to_date)
            ToDate.click()
            self.calender(str(self.data['year']), self.data['month'], str(self.data['date']))
            ApplyBtn = form.find_element(*self.leave_apply_btn)
            ApplyBtn.click()
            # actual_msg = form.find_element(*self.leave_successful_msg).text
            time.sleep(1)
            # assert actual_msg == self.data['expected_leave_successful_msg'], "Applied leave failed"

        except AssertionError as e:
            print(self.driver.find_element(*self.no_leaves).text)

        finally:
            Recruitment_page = Recruitment(self.driver)
            return Recruitment_page





