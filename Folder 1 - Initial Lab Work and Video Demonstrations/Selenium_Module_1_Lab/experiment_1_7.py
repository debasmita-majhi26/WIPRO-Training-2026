from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome
driver = webdriver.Chrome()

# Implicit Wait
driver.implicitly_wait(10)

# Open Selenium dynamic page
driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

print("Website opened successfully.")

# Click the button to create a dynamic element
button = driver.find_element(By.ID, "adder")
button.click()

print("Dynamic element creation button clicked.")

# Explicit Wait
wait = WebDriverWait(driver, 10)

dynamic_element = wait.until(
    EC.presence_of_element_located(
        (By.ID, "box0")
    )
)

print("Explicit wait completed successfully.")
print("Dynamic element found:", dynamic_element.get_attribute("id"))

# Highlight the element
driver.execute_script(
    "arguments[0].style.border='3px solid red'",
    dynamic_element
)

print("Dynamic element highlighted successfully.")

# Keep browser open for screenshot
time.sleep(5)

# Close browser
driver.quit()

print("Experiment 7 completed successfully.")