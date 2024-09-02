from tkinter.simpledialog import askstring
import tkinter as tk
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.baseclass import Locators


class Generic(Locators):

    def __init__(self, driver):
        self.driver = driver
        self.w = WebDriverWait(self.driver, 10)

    def click_on_element(self, locator_and_value):
        self.driver.find_element(*locator_and_value).click()

    def send_keys_to_element(self, locator_and_value, data):
        self.driver.find_element(*locator_and_value).send_keys(data)

    def url_verification(self, expected_url):
        current_url = self.driver.current_url
        print(current_url)
        print(expected_url)
        if current_url != expected_url:
            self.driver.get(expected_url)

    def wait_until_visibility_element_located(self, locator_and_value):
        try:
            return self.w.until(EC.visibility_of_element_located(locator_and_value))
        except Exception as e:
            print(f"Element not found: {e}")
            return None

    def wait_until_presence_element_located(self, locator_and_value):
        try:
            return self.w.until(EC.presence_of_element_located(locator_and_value))
        except Exception as e:
            print(f"Element not found: {e}")
            return None

    def take_screenshot_attach_toAllure(self, step_name, screenshot_name):
        with allure.step(step_name):
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

    def show_input_dialog(self, title, prompt):
        root = tk.Tk()
        root.withdraw()
        userInput = askstring(title, prompt)
        root.destroy()
        return userInput

    def clear_and_send(self, locator_and_value, input_data):
        input_fieled = self.driver.find_element(*locator_and_value)
        input_fieled.send_keys(Keys.CONTROL + "a")
        input_fieled.send_keys(Keys.DELETE)
        input_fieled.send_keys(input_data)

    def calender(self, year, month, date):
        form = self.driver.find_element(*self.switch_to_form)
        Year = form.find_element(*self.year_xpath)
        Year.click()
        SelectYear = form.find_elements(*self.select_dropdown)
        for cal_year in SelectYear:
            if year == cal_year.text:
                cal_year.click()
                break
        Month = form.find_element(*self.month_xpath)
        Month.click()
        SelectMonth = form.find_elements(*self.select_dropdown)
        for cal_month in SelectMonth:
            if month == cal_month.text:
                cal_month.click()
                break
        Date = form.find_elements(*self.date_xpath)
        for cal_date in Date:
            if date == cal_date.text:
                cal_date.click()
                break

