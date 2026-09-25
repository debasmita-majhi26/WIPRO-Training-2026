import os
from datetime import datetime


def capture_screenshot(driver, step_name):
    """
    Captures a screenshot with the given step name and stores it in the screenshots directory.
    Returns the absolute path to the captured screenshot.
    """
    # Root screenshots directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshots_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # Sanitize file name
    clean_name = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in step_name)
    file_name = f"{clean_name}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(file_path)
    print(f"[Screenshot] Captured: {file_name}")
    return file_path
