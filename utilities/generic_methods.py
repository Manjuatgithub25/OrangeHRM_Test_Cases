import logging
import time
from datetime import datetime
from pathlib import Path
from tkinter.simpledialog import askstring
import tkinter as tk
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.baseclass import Locators


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
        time.sleep(2)
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

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def capture_screenshot(self, name):
        """Capture a screenshot and save it to the 'Screenshots' folder."""
        screenshot_dir = Path('Screenshots')
        screenshot_dir.mkdir(exist_ok=True)  # Ensure the directory exists
        screenshot_path = screenshot_dir / name
        self.driver.get_screenshot_as_file(str(screenshot_path))  # Ensure self.driver is accessible

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        print("hook is being called")
        timestamp = datetime.now().strftime('%H-%M-%S')
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call':
            feature_request = item.funcargs.get('request', None)
            if feature_request:
                driver = feature_request.getfuncargvalue('browser')
                screenshot_path = f'C:/Users/manju/OneDrive/Documents/GitHub/OrangeHRM_Test_Cases/Screenshots/login_successful{timestamp}.png'
                driver.save_screenshot(screenshot_path)
                extra.append(pytest_html.extras.image(screenshot_path))

                # Add additional content if test fails or is skipped
                xfail = hasattr(report, 'wasxfail')
                if (report.skipped and xfail) or (report.failed and not xfail):
                    extra.append(pytest_html.extras.image(screenshot_path))
                    extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))

                report.extra = extra

            try:
                with open('logfile.log', 'r') as log_file:
                    log_content = log_file.read()
                    html = f'<pre>{log_content}</pre>'
                    extra.append(pytest_html.extras.html(html))
            except FileNotFoundError:
                print("Log file not found, unable to attach logs to the report.")

            report.extra = extra
