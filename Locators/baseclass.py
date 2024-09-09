from selenium.webdriver.common.by import By

from utilities.excel_data_reader import excel_to_dictionary


class Locators:
    data = excel_to_dictionary('recruitment')

    """common Xpath's"""
    switch_to_form = (By.XPATH, "//form[@class='oxd-form']")
    drop_down = (By.XPATH, "//div[text()='-- Select --']")
    add_btn = (By.XPATH, "//button[text()=' Add ']")
    save_btn = (By.XPATH, "//button[text()=' Save ']")
    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    calender_close_btn = (By.XPATH, "//div[@class='oxd-date-input-link --close']")
    file_input = (By.XPATH, "//input[@class='oxd-file-input']")

    user_name = (By.XPATH, "//input[@name='username']")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    user_profile_btn = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    logout_btn = (By.XPATH, "//ul[@role='menu']/li/a[text()='Logout']")

    admin = (By.XPATH, "//span[text()='Admin']")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']/../../descendant::div[@class='oxd-select-text-input']")
    click_admin_option = (By.XPATH, "//div[@role='option']/span[text()='Admin']")
    status_dropdown = (By.XPATH, "//label[text()='Status']/../../descendant::div[@class='oxd-select-text-input']")
    click_enabled_option = (By.XPATH, "//div[@role='option']/span[text()='Enabled']")
    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_option = (By.XPATH, "//div[@role='listbox']/div/span")
    username = (By.XPATH, "//label[text()='Username']/../../descendant::input")
    pw = (By.XPATH, "//label[text()='Password']/../../descendant::input")
    confirm_pw = (By.XPATH, "//label[text()='Confirm Password']/../../descendant::input")
    user_name_list = (By.XPATH, "//div[@class='oxd-table-body']/div/div/div[2]/div")
    delete_user = (By.XPATH, "../following-sibling::div/div/button[1]")
    delete_user_btn = (By.XPATH, "//div[@class='orangehrm-modal-footer']/button[2]")
    delete_msg = (By.XPATH, "//p[text()='Successfully Deleted']")
    Saved_msg = (By.XPATH, "//p[text()='Successfully Saved']")

    leave_btn = (By.XPATH, "//span[text()='Leave']")
    apply_btn = (By.XPATH, "//a[text()='Apply']")
    apply_page = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
    from_date = (By.XPATH, "//label[text()='From Date']/../..//i")
    to_date = (By.XPATH, "//label[text()='To Date']/../..//i")
    year_xpath = (By.XPATH, "//div[@class='oxd-calendar-selector-year-selected']")
    month_xpath = (By.XPATH, "//div[@class='oxd-calendar-selector-month-selected']")
    date_xpath = (By.XPATH, "//div[@class='oxd-calendar-date']")
    select_dropdown = (By.XPATH, "//li[contains(@class,'oxd-calendar-dropdown--option')]")
    leave_type_option = (By.XPATH, "//span[text()='CAN - FMLA']")
    leave_apply_btn = (By.XPATH, "//div[@class='oxd-form-actions']/button")
    leave_successful_msg = (By.XPATH, "//p[text()='Successfully Saved']")
    no_leaves = (By.XPATH, "//p[text()='No Leave Types with Leave Balance']")

    click_recruitment = (By.XPATH, "//span[text()='Recruitment']")
    choose_vacancy = (By.XPATH, "//span[text()='Software Engineer']")
    contact_number = (By.XPATH, "//label[text()='Contact Number']/../..//input")
    Email = (By.XPATH, "//label[text()='Email']/../..//input")
    keywords = (By.XPATH, "//label[text()='Keywords']/../..//input")
    consent_btn = (By.XPATH, "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']")
    date_of_application = (By.XPATH, "//label[text()='Date of Application']/../..//i")
    click_candidates = (By.XPATH, "//a[text()='Candidates']")
    candidate_list = (By.XPATH, "//div[@class='oxd-table-body']/div/div/div[3]/div")
    download_resume = (By.XPATH, "../following-sibling::div[4]//i[@class='oxd-icon bi-download']/..")

    my_info = (By.XPATH, "//span[text()='My Info']")
    employee_id = (By.XPATH, "//label[text()='Employee Id']/../../div/input")
    driver_license = (By.XPATH, "//label[contains(text(), 'License Number')]/../../div/input")
    license_expiry_date = (By.XPATH, "//label[text()='License Expiry Date']/../..//i")
    nationality = (By.XPATH, "//label[text()='Nationality']/../../div[2]")
    marital_status = (By.XPATH, "//label[text()='Marital Status']/../../div[2]//div[@class='oxd-select-text-input']")
    marital_status_option = (By.XPATH, "//span[contains(text(), 'Married')]")
    dob = (By.XPATH, "//label[text()='Date of Birth']/../..//i")
    gender = (By.XPATH, "//label[.='Gender']/../../descendant::label[.='Female']")
    nationality_option = (By.XPATH, "//label[text()='Nationality']/../..//div[text()='Indian']")
    info_save_btn = (By.XPATH, "//button[text()=' Save '][1]")
    attachments = (By.XPATH, "//h6[text()='Attachments']/..//i")
    attachment_save_btn = (By.XPATH, "//div[@class='orangehrm-attachment']//button[text()=' Save ']")
    attachments_list = (By.XPATH, "//div[@class='oxd-table-body']/div/div/div[2]")
    download_file = (By.XPATH, "..//div[@class='oxd-table-cell-actions']/button[3]")
    info_input_file = (By.XPATH, "//label[text()='Select File']/../../div/input")


