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

    def input_leave_details(self):
        self.click_on_element(self.leave_btn)
        self.click_on_element(self.apply_btn)
        try:
            form = self.driver.find_element(*self.switch_to_form)
            Leave_type = form.find_element(*self.drop_down)
            Leave_type.click()
            Leave_Type_Option = form.find_element(*self.leave_type_option)
            Leave_Type_Option.click()
            FromDate = form.find_element(*self.from_date)
            FromDate.click()
            self.calender(self.data['Year'], self.data['Month'], self.data['Date'])
            time.sleep(1)
            ToDate = form.find_element(*self.to_date)
            ToDate.click()
            self.calender(self.data['year'], self.data['month'], self.data['date'])
            ApplyBtn = form.find_element(*self.leave_apply_btn)
            ApplyBtn.click()

        except AssertionError:
            print(self.driver.find_element(*self.no_leaves).text)

        finally:
            Recruitment_page = Recruitment(self.driver)
            return Recruitment_page





