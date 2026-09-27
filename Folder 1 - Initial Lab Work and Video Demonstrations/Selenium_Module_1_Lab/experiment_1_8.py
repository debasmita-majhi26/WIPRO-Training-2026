from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open Selenium Web Form
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    print("Website opened successfully.")

    # Create screenshots folder if it does not exist
    os.makedirs("screenshots", exist_ok=True)

    # Take screenshot of the webpage
    screenshot_path = "screenshots/experiment_1_8.png"
    driver.save_screenshot(screenshot_path)

    print("Screenshot taken successfully.")
    print("Screenshot saved at:", screenshot_path)

    # Try to find a valid element
    text_box = driver.find_element(By.ID, "my-text-id")
    text_box.send_keys("Exception Handling")

    print("Valid element found successfully.")

    # Try to find an element that does not exist
    try:
        driver.find_element(By.ID, "element-that-does-not-exist")

    except NoSuchElementException:
        print("Exception handled: Element was not found.")

    # Keep browser open
    time.sleep(5)

finally:
    # Close browser
    driver.quit()

    print("Browser closed successfully.")
    print("Experiment 8 completed successfully.")