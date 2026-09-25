from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    """
    BasePage serves as the parent class for all Page Objects.
    Encapsulates WebDriver interactions, explicit waits, and common browser actions.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Finds an element present in the DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator, timeout=None):
        """Finds an element visible on the page."""
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Finds all elements present in the DOM matching locator."""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Waits until clickable, handles potential overlay, scrolls into view, and clicks."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
        except ElementClickInterceptedException:
            # Handle potential ad/overlay interference
            self.dismiss_ad_overlay()
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text, clear_first=True):
        """Waits for element visibility, optionally clears it, and types text."""
        element = self.find_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retrieves visible inner text of an element."""
        return self.find_visible(locator).text.strip()

    def is_displayed(self, locator, timeout=5):
        """Checks if an element is visible on the page within the given timeout."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        """Scrolls the page so that the element is centered in the viewport."""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def dismiss_ad_overlay(self):
        """
        Handles any unexpected interstitial ads or vignette overlays
        frequently served on AutomationExercise.
        """
        try:
            current_url = self.driver.current_url
            if "#google_vignette" in current_url:
                clean_url = current_url.split("#")[0]
                self.driver.get(clean_url)
                return

            # Try closing dismiss button if inside Google ad iframe
            dismiss_buttons = self.driver.find_elements(By.XPATH, "//div[@id='dismiss-button' or @aria-label='Close ad']")
            for btn in dismiss_buttons:
                if btn.is_displayed():
                    btn.click()
                    return
        except Exception:
            pass

    def get_title(self):
        """Returns the current page title."""
        return self.driver.title

    def get_current_url(self):
        """Returns the current page URL."""
        return self.driver.current_url
