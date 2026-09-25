import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(headless=None):
    """
    Initializes and configures the Chrome WebDriver instance.
    Supports headless mode via parameter or HEADLESS environment variable.
    Configures Chrome DevTools Protocol to block third-party ad networks
    for robust, flake-free testing on AutomationExercise.
    """
    options = Options()

    # Determine headless mode
    if headless is None:
        headless_env = os.environ.get("HEADLESS", "false").lower()
        headless = headless_env in ("true", "1", "yes")

    if headless:
        options.add_argument("--headless=new")

    # Standard browser options
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")

    # Disable automation banner/detection
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)

    # Use Chrome DevTools Protocol to block annoying ad networks on AutomationExercise
    try:
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd(
            "Network.setBlockedURLs",
            {
                "urls": [
                    "*googlesyndication.com*",
                    "*google-analytics.com*",
                    "*doubleclick.net*",
                    "*adservice.google.com*",
                    "*googleads*",
                    "*pagead2.googlesyndication.com*",
                ]
            },
        )
    except Exception as e:
        print(f"Warning: CDP network blocking could not be enabled: {e}")

    return driver
