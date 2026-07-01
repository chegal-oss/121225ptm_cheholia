import pytest

try:
    from selenium import webdriver
    from selenium.common import WebDriverException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
except ModuleNotFoundError:
    webdriver = None


SITE_URL = "https://www.saucedemo.com/"


@pytest.fixture
def browser():
    if webdriver is None:
        pytest.fail("Install selenium in the project environment: pip install selenium")

    options = Options()
    options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"
    options.add_argument("--width=1440")
    options.add_argument("--height=1100")

    try:
        driver = webdriver.Firefox(options=options)
    except WebDriverException as error:
        pytest.fail(f"Firefox WebDriver did not start: {error}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(SITE_URL)

    def login(self, username, password):
        self.browser.find_element(*self.USERNAME).send_keys(username)
        self.browser.find_element(*self.PASSWORD).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    PRODUCTS = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
    }

    def __init__(self, browser):
        self.browser = browser

    def add_product(self, product_name):
        self.browser.find_element(*self.PRODUCTS[product_name]).click()

    def open_cart(self):
        self.browser.find_element(*self.CART).click()


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        self.browser.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")

    def __init__(self, browser):
        self.browser = browser

    def fill_user_data(self, first_name, last_name, postal_code):
        self.browser.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*self.LAST_NAME).send_keys(last_name)
        self.browser.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.browser.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self):
        total_text = self.browser.find_element(*self.TOTAL).text
        return total_text.replace("Total: ", "")


def test_saucedemo_total_price(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.add_product("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product("Sauce Labs Onesie")
    inventory_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_user_data("Ivan", "Ivanov", "10115")
    total = checkout_page.get_total()

    assert total == "$58.29"
