import os
from datetime import datetime
import pytest
from selenium import webdriver
from configuration.config import get_config


def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    home_dir = get_config("path", "home_dir") + '\\downloads'
    download_dir = os.path.join(home_dir, f"downloaded_file_{timestamp}")
    os.makedirs(download_dir, exist_ok=True)
    browser_name = request.config.getoption("--browser_name").lower()
    if browser_name == "chrome":
        option = webdriver.ChromeOptions()
        option.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
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
    driver.close()
