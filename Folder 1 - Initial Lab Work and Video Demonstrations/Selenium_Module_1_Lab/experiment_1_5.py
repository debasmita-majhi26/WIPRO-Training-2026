from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
text_box.send_keys("Advanced Selenium")

print("Text box handled successfully.")

# Keyboard action
text_box.send_keys(Keys.CONTROL, "a")
text_box.send_keys("Selenium Advanced Controls")

print("Keyboard action performed successfully.")

# 2. Handle Range Slider
slider = driver.find_element(By.NAME, "my-range")
slider.send_keys(Keys.RIGHT)
slider.send_keys(Keys.RIGHT)

print("Range slider handled successfully.")

# 3. Handle Color Picker
color_picker = driver.find_element(By.NAME, "my-colors")

print("Color picker found successfully.")

# 4. Handle Date Picker
date_picker = driver.find_element(By.NAME, "my-date")
date_picker.send_keys("09/26/2026")

print("Date picker handled successfully.")

# Keep browser open so the controls can be seen
time.sleep(5)

# Close browser
driver.quit()

print("Experiment 5 completed successfully.")