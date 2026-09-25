import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.screenshot import capture_screenshot


class TestEcommerceAutomation:
    """
    Capstone Assignment 1: Web Application Automation with Selenium WebDriver.
    Validates end-to-end e-commerce user journey on AutomationExercise:
    Login -> Search -> Update Quantity -> Add to Cart -> Verify Cart -> Logout.
    """

    def test_complete_ecommerce_flow(self, driver, test_data):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        base_url = test_data["base_url"]
        user_name = test_data["user_name"]
        user_email = test_data["user_email"]
        user_password = test_data["user_password"]
        product_name = test_data["product_name"]
        target_quantity = str(test_data["quantity"])

        # -------------------------------------------------------------
        # STEP 1: Launch Chrome and navigate to AutomationExercise
        # -------------------------------------------------------------
        print("\n[Step 1] Launching browser and opening application...")
        home_page.open(base_url)
        assert home_page.is_home_page_displayed(), "Home page was not displayed successfully."
        capture_screenshot(driver, "01_home_page")

        # -------------------------------------------------------------
        # STEP 2: Navigate to Signup/Login and login with credentials
        # -------------------------------------------------------------
        print("[Step 2] Navigating to Login page...")
        home_page.navigate_to_login()
        assert login_page.is_login_page_displayed(), "Login page elements are not displayed."
        capture_screenshot(driver, "02_login_page")

        print(f"[Step 2] Submitting login credentials for {user_email}...")
        login_page.login(user_email, user_password)

        # Fallback registration check in case of wiped test account
        if not home_page.is_user_logged_in(user_name):
            error_msg = login_page.get_error_message()
            if "incorrect" in error_msg.lower() or "not exist" in error_msg.lower():
                print("[Fallback] Account not found, executing registration fallback...")
                login_page.register_account(user_name, user_email, user_password)

        # -------------------------------------------------------------
        # STEP 3: Verify user is successfully logged in
        # -------------------------------------------------------------
        print(f"[Step 3] Verifying successful login for {user_name}...")
        assert home_page.is_user_logged_in(user_name), f"User {user_name} is not logged in."
        capture_screenshot(driver, "03_successful_login")

        # Clear any accumulated cart contents for test idempotency
        print("[Housekeeping] Clearing previous cart items for repeatability...")
        home_page.navigate_to_cart()
        cart_page.clear_cart()

        # -------------------------------------------------------------
        # STEP 4: Navigate to Products and search for product
        # -------------------------------------------------------------
        print(f"[Step 4] Navigating to Products and searching for '{product_name}'...")
        home_page.navigate_to_products()
        product_page.search_product(product_name)
        assert product_page.is_search_results_visible(), "Searched products section not visible."
        capture_screenshot(driver, "04_search_results")

        # -------------------------------------------------------------
        # STEP 5: Open product details and update quantity
        # -------------------------------------------------------------
        print(f"[Step 5] Opening product details for '{product_name}' and setting quantity to {target_quantity}...")
        product_page.open_product_details(product_name)
        product_page.set_quantity(target_quantity)
        actual_quantity = product_page.get_quantity_value()
        assert actual_quantity == target_quantity, (
            f"Quantity mismatch: expected {target_quantity}, got {actual_quantity}"
        )
        capture_screenshot(driver, "05_product_quantity_updated")

        # -------------------------------------------------------------
        # STEP 6: Add product to cart and handle the 'Added!' modal
        # -------------------------------------------------------------
        print("[Step 6] Adding product to cart and verifying 'Added!' modal...")
        product_page.add_to_cart()
        assert product_page.is_added_modal_displayed(), "'Added!' modal popup was not displayed."
        capture_screenshot(driver, "06_added_to_cart_popup")

        # -------------------------------------------------------------
        # STEP 7: Open the cart and verify details
        # -------------------------------------------------------------
        print("[Step 7] Opening cart and verifying item details...")
        product_page.click_view_cart_in_modal()
        assert cart_page.is_cart_page_displayed(), "Cart page is not displayed."

        cart_details = cart_page.get_cart_item_details(product_name)
        print(f"[Step 7] Cart details retrieved: {cart_details}")

        # Assert product name
        assert product_name.lower() in cart_details["name"].lower(), (
            f"Expected product {product_name} in cart, found {cart_details['name']}"
        )

        # Assert quantity
        assert cart_details["quantity"] == target_quantity, (
            f"Expected quantity {target_quantity}, got {cart_details['quantity']}"
        )

        # Assert unit price and total price calculation
        unit_price_numeric = int("".join(filter(str.isdigit, cart_details["unit_price"])))
        total_price_numeric = int("".join(filter(str.isdigit, cart_details["total_price"])))
        expected_total = unit_price_numeric * int(target_quantity)

        assert total_price_numeric == expected_total, (
            f"Total price calculation failed: expected {expected_total}, got {total_price_numeric}"
        )
        capture_screenshot(driver, "07_verified_cart")

        # -------------------------------------------------------------
        # STEP 8 & 9: Logout and verify login page is displayed
        # -------------------------------------------------------------
        print("[Step 9] Logging out and verifying return to login page...")
        home_page.logout()
        assert login_page.is_login_page_displayed(), "Login page was not displayed after logout."
        capture_screenshot(driver, "08_logout")
        print("\nAll steps completed and verified successfully!")
