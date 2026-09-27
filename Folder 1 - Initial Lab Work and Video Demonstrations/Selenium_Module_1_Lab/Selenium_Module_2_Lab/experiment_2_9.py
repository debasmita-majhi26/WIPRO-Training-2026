from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def open(self):
        self.driver.get("https://www.google.com")

    def get_title(self):
        return self.driver.title


def test_home_page():

    driver = webdriver.Chrome()

    page = HomePage(driver)

    page.open()

    assert "Google" in page.get_title()

    driver.quit()