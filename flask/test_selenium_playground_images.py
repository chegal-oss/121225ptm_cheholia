from time import sleep

import pytest

try:
    from selenium import webdriver
    from selenium.common import WebDriverException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
except ModuleNotFoundError:
    webdriver = None


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


def test_button_text_changed(browser):
    browser.get("http://uitestingplayground.com/textinput")

    input_field = browser.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")

    button = browser.find_element(By.ID, "updatingButton")
    button.click()

    assert button.text == "ITCH"


def test_third_image_alt_is_award(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    sleep(10)

    images = [
        image for image in browser.find_elements(By.TAG_NAME, "img")
        if image.get_attribute("alt")
    ]
    third_image = images[2]

    assert third_image.get_attribute("alt") == "award"
