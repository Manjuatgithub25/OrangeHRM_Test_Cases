import time

from selenium.webdriver.support.wait import WebDriverWait

from page_objects.test_recruitment import Recruitment
from utilities.generic_methods import Generic


class Leave(Generic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.w = WebDriverWait(driver, 10)

    def click_on_leave(self):
        self.click_on_element(self.leave_btn)

    def input_leave_details(self, Year, Month, Date, year, month, date, expected_leave_successful_msg):
        self.click_on_element(self.apply_btn)
        try:
            form = self.driver.find_element(*self.switch_to_form)
            Leave_type = form.find_element(*self.drop_down)
            Leave_type.click()
            Leave_Type_Option = form.find_element(*self.leave_type_option)
            Leave_Type_Option.click()
            FromDate = form.find_element(*self.from_date)
            FromDate.click()
            self.calender(Year, Month, Date)
            # FromDate.send_keys("2024-12-10")
            ToDate = form.find_element(*self.to_date)
            ToDate.click()
            self.calender(year, month, date)
            '''ToDateYear = form.find_element(*self.to_date_year)
            ToDateYear.click()
            SelectYear = form.find_elements(*self.select_dropdown)
            for cal_year in SelectYear:
                if year == cal_year.text:
                    cal_year.click()
                    break
            ToDateMonth = form.find_element(*self.to_date_month)
            ToDateMonth.click()
            SelectMonth = form.find_elements(*self.select_dropdown)
            for cal_month in SelectMonth:
                if month == cal_month.text:
                    cal_month.click()
                    break
            ToDateDate = form.find_elements(*self.to_date_date)
            for cal_date in ToDateDate:
                if date == cal_date.text:
                    cal_date.click()
                    break'''
            ApplyBtn = form.find_element(*self.leave_apply_btn)
            ApplyBtn.click()
            actual_msg = form.find_element(*self.leave_successful_msg).text
            time.sleep(1)
            assert actual_msg == expected_leave_successful_msg, "Applied leave failed"

        except AssertionError as e:
            print(self.driver.find_element(*self.no_leaves).text)

        finally:
            Recruitment_page = Recruitment(self.driver)
            return Recruitment_page





