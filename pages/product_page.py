from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    """
    Page Object representing the Products catalog, search, and product details.
    """

    # Locators
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULTS_HEADER = (By.XPATH, "//h2[contains(text(), 'Searched Products')]")
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, "div.productinfo p")

    # Product details locators
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product-information h2")
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.cart")

    # Added to cart modal locators
    CART_MODAL = (By.ID, "cartModal")
    MODAL_TITLE = (By.XPATH, "//div[@id='cartModal']//h4[contains(text(), 'Added!')]")
    VIEW_CART_MODAL_LINK = (By.XPATH, "//div[@id='cartModal']//u[contains(text(), 'View Cart')]/..")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//div[@id='cartModal']//button[contains(text(), 'Continue Shopping')]")

    def search_product(self, product_name):
        """Types product name in search box and clicks search button."""
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
        self.dismiss_ad_overlay()

    def is_search_results_visible(self):
        """Verifies if 'Searched Products' title is visible."""
        return self.is_displayed(self.SEARCH_RESULTS_HEADER)

    def open_product_details(self, product_name="Blue Top"):
        """
        Clicks 'View Product' for the given product.
        Uses product name in XPath or link to product details.
        """
        # Locator for the 'View Product' link corresponding to product
        view_product_locator = (
            By.XPATH,
            f"//div[contains(@class, 'productinfo')]//p[contains(text(), '{product_name}')]/ancestor::div[contains(@class, 'single-products')]/following-sibling::div[contains(@class, 'choose')]//a",
        )
        if not self.is_displayed(view_product_locator, timeout=4):
            # Fallback to general View Product link
            view_product_locator = (By.XPATH, "//a[contains(@href, '/product_details/')]")

        self.click(view_product_locator)
        self.dismiss_ad_overlay()

    def set_quantity(self, quantity):
        """Clears existing quantity and types new quantity."""
        qty_element = self.find_visible(self.QUANTITY_INPUT)
        qty_element.clear()
        qty_element.send_keys(str(quantity))

    def get_quantity_value(self):
        """Returns the current value of the quantity input field."""
        return self.find_visible(self.QUANTITY_INPUT).get_attribute("value")

    def add_to_cart(self):
        """Clicks the 'Add to cart' button."""
        self.click(self.ADD_TO_CART_BUTTON)

    def is_added_modal_displayed(self):
        """Verifies if the 'Added!' modal popup is displayed."""
        return self.is_displayed(self.CART_MODAL, timeout=8)

    def click_view_cart_in_modal(self):
        """Clicks 'View Cart' link inside the 'Added!' confirmation modal."""
        self.click(self.VIEW_CART_MODAL_LINK)
        self.dismiss_ad_overlay()

    def click_continue_shopping(self):
        """Clicks 'Continue Shopping' button in the modal."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
