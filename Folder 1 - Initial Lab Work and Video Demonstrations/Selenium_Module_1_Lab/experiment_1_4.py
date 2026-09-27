from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Start Chrome
driver = webdriver.Chrome()

# Open Selenium Web Form
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Maximize browser
driver.maximize_window()

print("Website opened successfully.")

# 1. Handle Text Box
text_box = driver.find_element(By.ID, "my-text-id")
text_box.send_keys("Selenium WebDriver")
print("Text box handled successfully.")

# 2. Handle Password Field
password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("12345")
print("Password field handled successfully.")

# 3. Handle Text Area
text_area = driver.find_element(By.NAME, "my-textarea")
text_area.send_keys("This is Selenium WebDriver practice.")
print("Text area handled successfully.")

# 4. Handle Dropdown
dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")
print("Dropdown handled successfully.")

# 5. Handle Checkbox
checkbox = driver.find_element(By.ID, "my-check-1")

if not checkbox.is_selected():
    checkbox.click()

print("Checkbox handled successfully.")

# 6. Handle Radio Button
radio_button = driver.find_element(By.ID, "my-radio-1")

if not radio_button.is_selected():
    radio_button.click()

print("Radio button handled successfully.")

# Keep browser open
time.sleep(5)

# 7. Handle Submit Button
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

print("Submit button clicked successfully.")

# Wait for result
time.sleep(3)

# Close browser
driver.quit()

print("Experiment 4 completed successfully.")