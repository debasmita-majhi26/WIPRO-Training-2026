from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome
driver = webdriver.Chrome()

# Open Selenium practice website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Maximize browser
driver.maximize_window()

print("Website opened successfully.")

# 1. Locate the text box using ID
text_box = driver.find_element(By.ID, "my-text-id")
text_box.send_keys("Selenium")

print("ID locator used successfully.")

# 2. Locate the password field using Name
password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("12345")

print("Name locator used successfully.")

# 3. Locate the link using Link Text
link = driver.find_element(By.LINK_TEXT, "Return to index")
print("Link Text locator found:", link.text)

# Wait so that the result can be seen
time.sleep(5)

# Close browser
driver.quit()

print("Experiment 3 completed successfully.")