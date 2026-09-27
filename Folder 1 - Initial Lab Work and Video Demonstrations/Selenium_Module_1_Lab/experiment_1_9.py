from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Start Chrome
driver = webdriver.Chrome()

# Open Selenium mouse interaction page
driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

print("Advanced interactions page opened successfully.")

# Create ActionChains object
actions = ActionChains(driver)

# 1. Mouse Hover
hover_element = driver.find_element(By.ID, "hover")
actions.move_to_element(hover_element).perform()

print("Mouse hover performed successfully.")

time.sleep(2)

# 2. Double Click
clickable_element = driver.find_element(By.ID, "clickable")
actions.double_click(clickable_element).perform()

print("Double-click performed successfully.")

time.sleep(2)

# 3. Right Click
right_click_element = driver.find_element(By.ID, "clickable")
actions.context_click(right_click_element).perform()

print("Right-click performed successfully.")

time.sleep(2)

# 4. Drag and Drop
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions.drag_and_drop(source, target).perform()

print("Drag and drop performed successfully.")

# Keep browser open for screenshot
time.sleep(5)

# Close browser
driver.quit()

print("Experiment 9 completed successfully.")