from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create Chrome options
options = Options()

# Start Chrome using Selenium WebDriver
driver = webdriver.Chrome(options=options)

# Open Selenium website
driver.get("https://www.selenium.dev/")

# Maximize browser
driver.maximize_window()

print("Selenium WebDriver started successfully.")
print("Browser:", driver.capabilities["browserName"])
print("Browser Version:", driver.capabilities["browserVersion"])
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

# Keep browser open for 5 seconds
import time
time.sleep(5)

# Close browser
driver.quit()

print("WebDriver session closed successfully.")