from time import sleep

import pytest

try:
    from selenium import webdriver
    from selenium.common import WebDriverException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
except ModuleNotFoundError:
    webdriver = None


PAGE_URL = "https://itcareerhub.de/ru"


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


def test_header_and_callback_popup(browser):
    def find_visible(css_selector):
        elements = browser.find_elements(By.CSS_SELECTOR, css_selector)
        return next(element for element in elements if element.is_displayed())

    browser.get(PAGE_URL)
    sleep(2)

    cookie_button = browser.find_elements(By.CLASS_NAME, "t972__accept-btn")
    if cookie_button:
        cookie_button[0].click()

    logo = browser.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")
    assert logo.is_displayed()

    assert find_visible("a[href='#submenu:more']")
    assert find_visible("a[href='#rec1921734713']")
    assert find_visible("a[href='#submenu:more2']")
    assert find_visible("a[href='/reviews']")
    assert find_visible("a[href='https://blog.itcareerhub.de/']")
    assert find_visible("a[href='/ru']")
    assert find_visible("a[href='/']")
    assert "Контакты" in browser.find_element(By.TAG_NAME, "body").text

    about_link = find_visible("a[href='#submenu:more2']")
    browser.execute_script("arguments[0].click();", about_link)
    sleep(1)

    contacts_link = browser.find_element(By.CSS_SELECTOR, "a[href='/ru/contact-us']")
    browser.execute_script("arguments[0].click();", contacts_link)
    sleep(3)

    callback_button = find_visible("a[href='#popup:form-tr']")
    browser.execute_script("arguments[0].click();", callback_button)
    sleep(2)

    page_text = browser.find_element(By.TAG_NAME, "body").text
    assert "Запишитесь на бесплатную карьерную консультацию" in page_text
