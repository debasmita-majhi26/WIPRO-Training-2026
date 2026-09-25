import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object representing the Cart page (/view_cart).
    Supports inspecting cart item details and clearing items for test repeatability.
    """

    # Locators
    CART_TABLE = (By.ID, "cart_info_table")
    CART_ROWS = (By.XPATH, "//tr[contains(@id, 'product-')]")
    EMPTY_CART_MESSAGE = (By.ID, "empty_cart")

    def is_cart_page_displayed(self):
        """Checks if cart page or cart table/empty message is visible."""
        return self.is_displayed(self.CART_TABLE, timeout=5) or self.is_displayed(
            self.EMPTY_CART_MESSAGE, timeout=5
        )

    def get_cart_item_details(self, product_name="Blue Top"):
        """
        Returns a dictionary containing product name, unit price, quantity,
        and total price for the specified product row in the cart.
        """
        self.find_visible(self.CART_TABLE)
        row_xpath = f"//tr[contains(@id, 'product-') and .//a[contains(text(), '{product_name}')]]"
        row = self.find_visible((By.XPATH, row_xpath))

        name = row.find_element(By.CSS_SELECTOR, "td.cart_description h4 a").text.strip()
        unit_price = row.find_element(By.CSS_SELECTOR, "td.cart_price p").text.strip()
        quantity = row.find_element(By.CSS_SELECTOR, "td.cart_quantity button").text.strip()
        total_price = row.find_element(By.CSS_SELECTOR, "td.cart_total p").text.strip()

        return {
            "name": name,
            "unit_price": unit_price,
            "quantity": quantity,
            "total_price": total_price,
        }

    def clear_cart(self):
        """
        Removes all existing products from the cart to ensure reliable,
        repeatable test runs without accumulated items.
        """
        delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, "a.cart_quantity_delete")
        for btn in delete_buttons:
            try:
                btn.click()
                time.sleep(1)
            except Exception:
                pass
