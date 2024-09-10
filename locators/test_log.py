import logging
import inspect
from datetime import datetime
import pytest
import pytest_html


class Log:
    def __init__(self, driver):
        self.driver = driver

    def get_logger(self, message):
        """Creates and returns a logger with the specified message."""
        logger_name = inspect.stack()[1][3]  # Get the caller function name
        logger = logging.getLogger(logger_name)

        if not logger.hasHandlers():  # Prevent adding duplicate handlers
            file_handler = logging.FileHandler("logging.log")
            formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)
        logger.info(message)
        return message

    def take_screenshot(self, name):
        """Takes a screenshot and returns the file name."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_file = f"{name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_file)
        return screenshot_file


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to add extra details like screenshots to the pytest report."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        extra = getattr(report, 'extra', [])
        report.extra = extra


class TestLogger:
    def __init__(self, driver):
        self.logger = Log(driver)

    def attach_screenshot_to_report(self, request, message):
        """Attach screenshot and log message to the HTML report."""
        log_message = self.logger.get_logger(message)
        screenshot_file = self.logger.take_screenshot(request.node.name)

        # Add the screenshot and log message to the pytest-html report
        if hasattr(request.config, '_html'):
            extra = getattr(request.node, '_report', None)
            if extra is not None:
                # Get the extra attribute and append the image with log message
                extra = getattr(extra, 'extra', [])
                extra.append(pytest_html.extras.image(screenshot_file, message=log_message))
                request.node._report.extra = extra


