from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Create Chrome options
options = Options()

# Start Chrome browser
driver = webdriver.Chrome(options=options)

# Open a website
driver.get("https://www.google.com")

# Maximize the browser window
driver.maximize_window()

print("Chrome browser opened successfully.")
print("Current page title:", driver.title)
print("Current URL:", driver.current_url)

# Keep the browser open for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()

print("Browser closed successfully.")