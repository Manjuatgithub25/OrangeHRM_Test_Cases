from selenium.webdriver.common.by import By


class Locators:
    user_name = (By.XPATH, "//input[@name='username']")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    user_profile_btn = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    logout_btn = (By.XPATH, "//ul[@role='menu']/li/a[text()='Logout']")

    admin = (By.XPATH, "//span[text()='Admin']")
    add_btn = (By.XPATH, "//button[text()=' Add ']")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']/../../descendant::div[@class='oxd-select-text-input']")
    click_admin_option = (By.XPATH, "//div[@role='option']/span[text()='Admin']")
    status_dropdown = (By.XPATH, "//label[text()='Status']/../../descendant::div[@class='oxd-select-text-input']")
    click_enabled_option = (By.XPATH, "//div[@role='option']/span[text()='Enabled']")
    switch_to_add_user_form = (By.XPATH, "//form[@class='oxd-form']")
    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_option = (By.XPATH, "//div[@role='listbox']/div/span")
    username = (By.XPATH, "//label[text()='Username']/../../descendant::input")
    pw = (By.XPATH, "//label[text()='Password']/../../descendant::input")
    confirm_pw = (By.XPATH, "//label[text()='Confirm Password']/../../descendant::input")
    save_btn = (By.XPATH, "//button[text()=' Save ']")
    user_name_list = (By.XPATH, "//div[@class='oxd-table-body']/div/div/div[2]/div")
    delete_user = (By.XPATH, "../following-sibling::div/div/button[1]")
    delete_user_btn = (By.XPATH, "//div[@class='orangehrm-modal-footer']/button[2]")
    delete_msg = (By.XPATH, "//p[text()='Successfully Deleted']")
    Saved_msg = (By.XPATH, "//p[text()='Successfully Saved']")

    leave_btn = (By.XPATH, "//span[text()='Leave']")
    switch_to_leave_form = (By.XPATH, "//form[@class='oxd-form']")
    from_date = (By.XPATH, "//label[text()='From Date']")
    end_date = (By.XPATH, "//label[text()='To Date']")
    date = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")

