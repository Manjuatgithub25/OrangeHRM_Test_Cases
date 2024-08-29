from selenium import webdriver
from selenium.webdriver.support.relative_locator import locate_with

from utilities.generic_methods import Generic


class Leave(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_leave(self):
        self.click_on_element(self.leave_btn)

    def input_leave_details(self):
        form = self.driver.find_element(self.switch_to_leave_form)
        FromDate = form.find_element(*self.from_date)
        input_FromDate = form.find_element(locate_with(*self.date).below(FromDate))
        input_FromDate.clear().send_keys("2024-10-10")
        EndDate = form.find_element(*self.end_date)
        input_EndDate = form.find_element(locate_with(*self.date).below(EndDate))
        input_EndDate.clear().send_keys("2024-12-10")

