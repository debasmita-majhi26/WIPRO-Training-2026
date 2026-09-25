import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object representing the Signup / Login page.
    Includes login actions and an automatic registration fallback if the account does not exist.
    """

    # Login locators
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Login to your account')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//form[@action='/login']//p[contains(@style, 'color: red')]")

    # Signup locators
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    # Account registration locators
    GENDER_RADIO = (By.ID, "id_gender1")
    REG_PASSWORD = (By.ID, "password")
    REG_FIRST_NAME = (By.ID, "first_name")
    REG_LAST_NAME = (By.ID, "last_name")
    REG_COMPANY = (By.ID, "company")
    REG_ADDRESS = (By.ID, "address1")
    REG_COUNTRY = (By.ID, "country")
    REG_STATE = (By.ID, "state")
    REG_CITY = (By.ID, "city")
    REG_ZIPCODE = (By.ID, "zipcode")
    REG_MOBILE = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def is_login_page_displayed(self):
        """Verifies if the Login page header and inputs are visible."""
        return self.is_displayed(self.EMAIL_INPUT) and self.is_displayed(self.LOGIN_BUTTON)

    def login(self, email, password):
        """Fills in credentials and submits the login form."""
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.dismiss_ad_overlay()

    def get_error_message(self):
        """Returns the login error message if present."""
        if self.is_displayed(self.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def register_account(self, name, email, password):
        """
        Sensible fallback registration in case the test account does not yet exist.
        Avoids test failures if the third-party test site resets its database.
        """
        self.type(self.SIGNUP_NAME_INPUT, name)
        self.type(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)
        self.dismiss_ad_overlay()

        # Step 2 form
        self.click(self.GENDER_RADIO)
        self.type(self.REG_PASSWORD, password)
        self.type(self.REG_FIRST_NAME, "Capstone")
        self.type(self.REG_LAST_NAME, "Student")
        self.type(self.REG_COMPANY, "College Test")
        self.type(self.REG_ADDRESS, "123 Automation Way")
        Select(self.find(self.REG_COUNTRY)).select_by_value("United States")
        self.type(self.REG_STATE, "California")
        self.type(self.REG_CITY, "Los Angeles")
        self.type(self.REG_ZIPCODE, "90001")
        self.type(self.REG_MOBILE, "1234567890")

        # Submit
        self.click(self.CREATE_ACCOUNT_BTN)
        self.dismiss_ad_overlay()

        # Continue
        if self.is_displayed(self.CONTINUE_BTN, timeout=5):
            self.click(self.CONTINUE_BTN)
            self.dismiss_ad_overlay()
