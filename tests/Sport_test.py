import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.OnlinePage import OnlinePage


@pytest.fixture(scope="module")
def browser():
    # driver_path = '/Users/aramgabrielyan/Downloads/chromedriver-mac-arm64/chromedriver'
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_website_is_up(browser):
    home_page = HomePage(browser)
    home_page.load()
    assert "Մարզադպրոցների կառավարման համակարգ" in browser.title


def test_homepage_contains_text(browser):
    home_page = HomePage(browser)
    home_page.load()
    assert home_page.contains_text("Մարզադպրոցների կառավարման համակարգ")


def test_login_page_loads(browser):
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.is_loaded()


def test_invalid_page_returns_404(browser):
    browser.get("https://sport.yerevan.am/invalidpage")
    assert "404" in browser.page_source


def test_online_page_loads(browser):
    online_page = OnlinePage(browser)
    online_page.load()
    assert online_page.is_loaded()
