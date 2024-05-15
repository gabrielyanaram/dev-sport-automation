import pytest
from selenium.webdriver.common.by import By

from helpers.WaitHelpers import *


@pytest.fixture(scope="class")
def wait(driver):
    yield WaitHelpers(driver)


class SportsmensPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://dev.sport.yerevan.am/sportsmens")

    CONSTANT_SSN = "7828200510"
    CONSTANT_DATE = "28/08/2020"

    SPORTSMENS_BUTTON = (By.CSS_SELECTOR, "a:nth-child(4) > p")
    LEAVE_LIST_BUTTON = (By.CSS_SELECTOR, "#\31")
    ADD_SPORTSMAN_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) > button > span")
    SSN_INPUT = (By.CSS_SELECTOR, "div.child-registration > form > div:nth-child(1) > div > input[type=text]")
    BIRTH_DATE_INPUT = (By.CSS_SELECTOR, "div:nth-child(2) > div > div > input[type=text]")
    CHECK_BUTTON = (By.CSS_SELECTOR, "form > button")

    def click_on_sportsmens(self):
        self.driver.implicitly_wait(5)
        wait_until_visible(self, SportsmensPage.SPORTSMENS_BUTTON).click()

    def click_on_add_sportsman(self):
        self.driver.implicitly_wait(5)
        wait_until_visible(self, SportsmensPage.ADD_SPORTSMAN_BUTTON).click()

    def enter_ssn(self, ssn):
        self.driver.implicitly_wait(5)
        wait_until_visible(self, SportsmensPage.SSN_INPUT).send_keys(ssn)

    def enter_birth_date(self, date):
        self.driver.implicitly_wait(5)
        wait_until_visible(self, SportsmensPage.BIRTH_DATE_INPUT).send_keys(date)

    def click_on_check_button(self):
        self.driver.implicitly_wait(5)
        wait_until_visible(self, SportsmensPage.CHECK_BUTTON).click()
