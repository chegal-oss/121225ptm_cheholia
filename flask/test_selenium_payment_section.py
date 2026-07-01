from pathlib import Path
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
SCREENSHOT_PATH = Path(__file__).with_name("payment_section.png")


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


def test_make_payment_section_screenshot(browser):
    browser.get(PAGE_URL)
    sleep(2)

    cookie_button = browser.find_elements(By.CLASS_NAME, "t972__accept-btn")
    if cookie_button:
        cookie_button[0].click()

    payment_menu_link = browser.find_element(By.CSS_SELECTOR, "a[href='#rec1921734713']")
    browser.execute_script("arguments[0].click();", payment_menu_link)
    sleep(2)

    payment_section = browser.find_element(By.ID, "rec1921734713")

    browser.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        payment_section,
    )

    assert payment_section.screenshot(str(SCREENSHOT_PATH))
    assert SCREENSHOT_PATH.exists()
    assert SCREENSHOT_PATH.stat().st_size > 0
