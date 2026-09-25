# Capstone Assignment 1: Web Application Automation with Selenium WebDriver

## Project Purpose
This project is an automated testing suite built for **College Capstone Assignment 1**: *"Automate a Web Application Using Selenium WebDriver with Python."* 

It automates a realistic, end-to-end e-commerce user journey on [AutomationExercise](https://automationexercise.com/) using Python, Selenium WebDriver, and PyTest following the Page Object Model (POM) architectural pattern.

---

## Technologies Used
- **Language**: Python 3.13
- **Automation Tool**: Selenium WebDriver (v4.20+)
- **Test Framework**: PyTest (v8.0+)
- **Reporting**: pytest-html (v4.1+)
- **Design Pattern**: Page Object Model (POM)
- **Data Driven**: JSON (`test_data/testdata.json`)
- **Browser**: Google Chrome

---

## Project Structure

```text
Capstone/
│
├── test_data/
│   └── testdata.json            # External test input data (credentials, URLs, product details)
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # Base Page Object with explicit waits, utilities & overlay handling
│   ├── home_page.py             # Home page navigation and user verification
│   ├── login_page.py            # Login interactions & account registration fallback
│   ├── product_page.py          # Search, product details, quantity update, & modal handling
│   └── cart_page.py             # Cart verification and item cleanup
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # PyTest fixtures for driver lifecycle and test data
│   └── test_ecommerce.py        # End-to-end test flow covering all 9 required steps
│
├── utils/
│   ├── __init__.py
│   ├── driver_setup.py          # Chrome WebDriver initialization with CDP ad-blocking
│   └── screenshot.py            # Screenshot capture utility
│
├── screenshots/                 # Captured execution screenshots (8 distinct milestones)
│   ├── 01_home_page.png
│   ├── 02_login_page.png
│   ├── 03_successful_login.png
│   ├── 04_search_results.png
│   ├── 05_product_quantity_updated.png
│   ├── 06_added_to_cart_popup.png
│   ├── 07_verified_cart.png
│   └── 08_logout.png
│
├── reports/                     # Generated HTML test execution reports
│   └── execution_report.html
│
├── requirements.txt             # Python project dependencies
├── pytest.ini                   # PyTest configuration settings
├── README.md                    # Project documentation and quickstart guide
├── PROJECT_REPORT.md            # Detailed academic submission report
└── run_test.py                  # One-click test runner script
```

---

## Installation & Setup

1. **Clone or Open the Repository**:
   Open a terminal in the project root directory (`Capstone`).

2. **Verify Python & Chrome**:
   Ensure Python 3.9+ and Google Chrome are installed on your system.

3. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run the Test

You can run the automation test suite in either of the two ways:

### Option 1: Using the Runner Script (Recommended)
```bash
python run_test.py
```
*Note: To run in headless mode in PowerShell, set `$env:HEADLESS="true"; python run_test.py`.*

### Option 2: Using PyTest Directly
```bash
pytest
```
Or with custom arguments:
```bash
pytest -v -s --html=reports/execution_report.html --self-contained-html
```

---

## Expected Test Flow

1. **Launch Browser**: Opens Google Chrome and navigates to `https://automationexercise.com/`.
2. **Navigate to Login**: Navigates to the *Signup / Login* page and enters user credentials from `testdata.json`.
3. **Verify Login**: Verifies that `"Logged in as <User Name>"` is displayed in the navigation bar.
4. **Search Product**: Navigates to the *Products* page and searches for `"Blue Top"`. Verifies `"SEARCHED PRODUCTS"` header.
5. **Update Quantity**: Opens product details and updates the quantity field to `3`.
6. **Add to Cart & Handle Modal**: Clicks *Add to cart* and verifies the `"Added!"` confirmation modal.
7. **Verify Cart Details**: Navigates to the Cart and verifies:
   - Product Name: `Blue Top`
   - Unit Price: `Rs. 500`
   - Quantity: `3`
   - Total Price: `Rs. 1500` (`unit_price * quantity`)
8. **Capture Screenshots**: High-resolution screenshots captured at each key milestone.
9. **Logout**: Clicks *Logout* and verifies return to the login page.

---

## Reports & Screenshots Location

- **HTML Execution Report**: `reports/execution_report.html`  
  Open this file in any web browser to view detailed execution metrics, test status, duration, and environment metadata.
- **Screenshots**: `screenshots/`  
  Contains 8 PNG images representing each critical stage of test execution.

---

## Assignment 1 Checklist (All 10 Requirements Satisfied)

| # | Official Requirement | Implementation Status | Location |
|---|----------------------|-----------------------|----------|
| 1 | Launch browser | Satisfied | `utils/driver_setup.py` |
| 2 | Login to application | Satisfied | `pages/login_page.py`, `tests/test_ecommerce.py` |
| 3 | Search product | Satisfied | `pages/product_page.py`, `tests/test_ecommerce.py` |
| 4 | Add product to cart | Satisfied | `pages/product_page.py`, `tests/test_ecommerce.py` |
| 5 | Update quantity | Satisfied | `pages/product_page.py`, `tests/test_ecommerce.py` |
| 6 | Verify cart details | Satisfied | `pages/cart_page.py`, `tests/test_ecommerce.py` |
| 7 | Capture screenshots | Satisfied (8 milestones) | `utils/screenshot.py`, `screenshots/` |
| 8 | Read test data from JSON | Satisfied | `test_data/testdata.json`, `tests/conftest.py` |
| 9 | Handle popup/alerts | Satisfied (Added! modal & CDP ad blocking) | `pages/base_page.py`, `pages/product_page.py` |
| 10 | Generate execution report | Satisfied (pytest-html) | `reports/execution_report.html` |
