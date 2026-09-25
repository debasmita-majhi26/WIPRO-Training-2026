import json
import os
import pytest
from utils.driver_setup import get_driver


@pytest.fixture(scope="session")
def test_data():
    """Loads test data from test_data/testdata.json."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    json_path = os.path.join(base_dir, "test_data", "testdata.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


@pytest.fixture(scope="function")
def driver():
    """Initializes and quits the WebDriver for each test function."""
    driver_instance = get_driver()
    yield driver_instance
    try:
        driver_instance.quit()
    except Exception:
        pass


def pytest_html_report_title(report):
    """Customizes the pytest-html report title."""
    report.title = "Capstone Assignment 1 - Automation Execution Report"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configures project metadata for the HTML report."""
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "College Capstone Assignment 1"
        config._metadata["Application"] = "AutomationExercise (https://automationexercise.com)"
        config._metadata["Framework"] = "Selenium WebDriver + PyTest + POM"
        config._metadata["Author"] = "College Student"
