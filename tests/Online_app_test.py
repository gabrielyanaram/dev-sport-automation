from selenium.common import NoSuchElementException

from pageObjects.OnlinePage import OnlinePage
from pageObjects.BasePage import RandomNumberGenerator, BasePage

import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    # driver_path = '/Users/aramgabrielyan/Downloads/chromedriver-mac-arm64/chromedriver'
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_online_page_loads(browser):
    online_page = OnlinePage(browser)
    online_page.load()


def test_create_online_app(browser):
    online_page = OnlinePage(browser)
    online_page.load()
    online_page.enter_phone_number(RandomNumberGenerator.generate_random_numbers())
    online_page.click_get_code_button()
    time.sleep(2)
    online_page.enter_pin("01234")

    assert online_page.new_pin_button() is False

    online_page.click_confirm_button()
    time.sleep(2)
    online_page.enter_ssn("7828200510")
    online_page.enter_date("28/08/2020")
    online_page.click_on_school_select()
    time.sleep(2)
    online_page.select_sport_school(3)
    time.sleep(2)
    online_page.click_on_sport_type_select()
    time.sleep(2)
    online_page.select_sport_type(0)
    online_page.click_on_checkbox()
    time.sleep(2)
    online_page.click_on_check_button()
    time.sleep(2)
    online_page.click_on_app_confirm_button()



