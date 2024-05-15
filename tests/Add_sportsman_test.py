import time
import pytest
from selenium import webdriver
from pageObjects.SportsmensPage import SportsmensPage
from tests.Base_test import Before


@pytest.fixture(scope="module")
def browser():
    # driver_path = '/Users/aramgabrielyan/Downloads/chromedriver-mac-arm64/chromedriver'
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_sportsman(browser):
    before = Before(browser)
    before.setUp()

    sportsmens_page = SportsmensPage(browser)
    sportsmens_page.click_on_sportsmens()
    sportsmens_page.click_on_add_sportsman()
    sportsmens_page.enter_ssn(SportsmensPage.CONSTANT_SSN)
    sportsmens_page.enter_birth_date(SportsmensPage.CONSTANT_DATE)
    sportsmens_page.click_on_check_button()
    time.sleep(5)
