from time import sleep

import pytest

try:
    from selenium import webdriver
    from selenium.common import WebDriverException
    from selenium.webdriver import ActionChains
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
    options.page_load_strategy = "eager"
    options.add_argument("--width=1440")
    options.add_argument("--height=1100")

    try:
        driver = webdriver.Firefox(options=options)
    except WebDriverException as error:
        pytest.fail(f"Firefox WebDriver did not start: {error}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def close_cookie_window(browser):
    buttons = browser.find_elements(
        By.XPATH,
        "//button[contains(., 'Consent') or contains(., 'Accept') or contains(., 'Agree') or contains(., 'Принять')]",
    )
    if buttons:
        browser.execute_script("arguments[0].click();", buttons[0])
        sleep(1)


def test_text_in_iframe(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    sleep(2)

    iframe = browser.find_element(By.TAG_NAME, "iframe")
    browser.switch_to.frame(iframe)

    text = "semper posuere integer et senectus justo curabitur."
    page_text = browser.find_element(By.TAG_NAME, "body").text

    assert text in page_text


def test_drag_photo_to_trash(browser):
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")
    sleep(5)
    close_cookie_window(browser)

    iframe = browser.find_element(By.CSS_SELECTOR, "iframe[src*='photo-manager.html']")
    browser.switch_to.frame(iframe)

    photos = browser.find_elements(By.CSS_SELECTOR, "#gallery li")
    trash = browser.find_element(By.ID, "trash")

    ActionChains(browser).drag_and_drop(photos[0], trash).perform()
    sleep(2)

    photos_in_gallery = browser.find_elements(By.CSS_SELECTOR, "#gallery li")
    photos_in_trash = browser.find_elements(By.CSS_SELECTOR, "#trash li")

    assert len(photos_in_gallery) == 3
    assert len(photos_in_trash) == 1
