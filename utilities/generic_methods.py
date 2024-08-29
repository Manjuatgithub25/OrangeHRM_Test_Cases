from tkinter.simpledialog import askstring
import tkinter as tk
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.baseclass import Locators


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

