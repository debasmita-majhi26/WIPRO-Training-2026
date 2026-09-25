from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object representing the AutomationExercise Home Page and common top navigation.
    """

    # Locators
    HOME_LOGO = (By.CSS_SELECTOR, "div.logo img")
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    CART_LINK = (By.CSS_SELECTOR, "a[href='/view_cart']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")

    def open(self, url):
        """Navigates to the base application URL."""
        self.driver.get(url)
        self.dismiss_ad_overlay()

    def is_home_page_displayed(self):
        """Verifies if the home page is displayed."""
        return self.is_displayed(self.HOME_LOGO)

    def navigate_to_login(self):
        """Clicks the Signup / Login link in the top navigation."""
        self.click(self.LOGIN_LINK)
        self.dismiss_ad_overlay()

    def navigate_to_products(self):
        """Clicks the Products link in the top navigation."""
        self.click(self.PRODUCTS_LINK)
        self.dismiss_ad_overlay()

    def navigate_to_cart(self):
        """Clicks the Cart link in the top navigation."""
        self.click(self.CART_LINK)
        self.dismiss_ad_overlay()

    def is_user_logged_in(self, expected_name=None):
        """Verifies if 'Logged in as <username>' is visible."""
        if not self.is_displayed(self.LOGGED_IN_TEXT, timeout=8):
            return False
        if expected_name:
            logged_in_text = self.get_text(self.LOGGED_IN_TEXT)
            return expected_name.lower() in logged_in_text.lower()
        return True

    def get_logged_in_user_text(self):
        """Returns the full 'Logged in as <username>' text."""
        return self.get_text(self.LOGGED_IN_TEXT)

    def logout(self):
        """Clicks the Logout link."""
        self.click(self.LOGOUT_LINK)
        self.dismiss_ad_overlay()
