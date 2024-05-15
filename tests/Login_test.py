import time

import pytest
from selenium import webdriver


from pageObjects.LoginPage import LoginPage


@pytest.fixture(scope="module")
def browser():
    # driver_path = '/Users/aramgabrielyan/Downloads/chromedriver-mac-arm64/chromedriver'
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_page_loads(browser):
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.is_loaded()


def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.enter_username("Jinanyan")
    login_page.enter_password("Jinanyan*11")
    login_page.click_login_button()
    time.sleep(2)
    assert login_page.contains_text("Երևանի գեղասահքի և հոկեյի մարզադպրոց")

