import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    directory_path = "C:\\Users\\manju\\OneDrive\\Documents\\GitHub\\OrangeHRM_Test_Cases\\downloads"
    browser_name = request.config.getoption("--browser_name").lower()
    if browser_name == "chrome":
        option = webdriver.ChromeOptions()
        option.add_experimental_option("prefs", {
            "download.default_directory": directory_path,  # Set your directory here
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "detach": True
        })
        driver = webdriver.Chrome(options=option)
    elif browser_name == "edge":
        option = webdriver.EdgeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Edge()
    else:
        return "Invalid browser"

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    # driver.close()
