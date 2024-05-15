import random
import pytest
from selenium.webdriver.common.by import By

from helpers.WaitHelpers import *

import sys

sys.path.append('/PycharmProjects/pythonProject5')


@pytest.fixture(scope="class")
def wait(driver):
    yield WaitHelpers(driver)


class GroupPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://dev.sport.yerevan.am/groups")

    def refresh_page(self):
        self.driver.refresh()

    def is_loaded(self):
        return "ԽՈՒՄԲ" in self.driver.page_source

    GROUPS_BUTTON = (By.CSS_SELECTOR, "div:nth-child(3) > a > p")
    ALL_GROUPS = (By.CSS_SELECTOR, "div.gym-trainer-item__top > h6")
    BODY = (By.CSS_SELECTOR, "body")
    TOASTER = (By.CSS_SELECTOR, "#toastify >div >div > div > div:nth-child(2) >p")

    """Group add locators"""
    ADD_GROUP_BUTTON = (By.CSS_SELECTOR, "div.menu-content-item-name > button")
    GROUP_NAME_INPUT = (By.CSS_SELECTOR, "input[type=text]")
    SPORT_TYPE_SELECT = (By.CSS_SELECTOR, "div:nth-child(3) > div > div > div > div")
    SELECT_LIST = (By.CSS_SELECTOR, ".group-registration__form-item > div > div > div > div:nth-child(2) > div > div")
    TRAINER_SELECT_N = (By.CSS_SELECTOR, "div > form > div:nth-child(4) > div")
    TRAINER_SELECT = (By.CSS_SELECTOR, "form > div:nth-child(4) > div > div > div > div")
    LEVEL_SELECT = (By.CSS_SELECTOR, "form > div:nth-child(5) > div > div > div > div")
    ASSISTANT_SELECT = (By.CSS_SELECTOR, "form > div:nth-child(6) > div > div > div > div")
    CREATE_BUTTON = (By.CSS_SELECTOR, "div.group-registration_buttons > button")

    """Group delete locators"""
    GROUP_DELETE_BUTTON = (By.CSS_SELECTOR, "button:nth-child(5)")
    APPROVE_BUTTON = (By.CSS_SELECTOR, "div.back-button__container > button:nth-child(1)")
    DECLINE_BUTTON = (By.CSS_SELECTOR, "div.back-button__container > button:nth-child(2)")

    def find_and_click_on_group_with_name(self, name):
        elements = self.driver.find_elements(*self.ALL_GROUPS)
        for element in elements:
            if name in element.text:
                element.click()
                return True
        return False

    def click_on_groups(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.GROUPS_BUTTON).click()
            print("Clicked on groups button successfully")
        except Exception as e:
            print("Groups button not clickable within the specified time:", e)

    def click_on_add_group(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.ADD_GROUP_BUTTON).click()
            print("Clicked on add group button successfully")
        except Exception as e:
            print("Add group button not clickable within the specified time:", e)

    def enter_group_name(self, group_name):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.GROUP_NAME_INPUT).send_keys(group_name)
            print("Group name entered successfully")
        except Exception as e:
            print("Group name not entered within the specified time:", e)

    def click_on_sport_type_select(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.SPORT_TYPE_SELECT).click()
            print("Sport type select clicked successfully")
        except Exception as e:
            print("Sport type select not clickable within the specified time:", e)

    def select(self, index):
        try:
            wait_until_visible(self, GroupPage.SELECT_LIST)
            self.driver.implicitly_wait(5)
            self.driver.find_elements(*GroupPage.SELECT_LIST)[index].click()
            print("Selected successfully")
        except Exception as e:
            print("Not selected within the specified time:", e)

    def click_on_trainer_select(self):
        try:
            wait_until_visible(self, GroupPage.ASSISTANT_SELECT)
            self.driver.implicitly_wait(5)
            self.driver.find_element(*GroupPage.TRAINER_SELECT).click()
            print("Trainer select clicked successfully")
        except Exception as e:
            print("Trainer select not clickable within the specified time:", e)

    def click_on_level_select(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.LEVEL_SELECT).click()
            print("Level select clicked successfully")
        except Exception as e:
            print("Level select not clickable within the specified time:", e)

    def click_on_assistant_select(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.ASSISTANT_SELECT).click()
            print("Assistant select clicked successfully")
        except Exception as e:
            print("Assistant select not clickable within the specified time:", e)

    def checkbox_click(self, index_list):
        try:
            wait_until_intractable(self, GroupPage.SELECT_LIST)
            self.driver.implicitly_wait(5)
            elements = self.driver.find_elements(*self.SELECT_LIST)
            for i in index_list:
                elements[i].click()
            print("Checkbox selected successfully")
        except Exception as e:
            print("Checkbox not selected within the specified time:", e)

    def click_on_create_button(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.CREATE_BUTTON).click()
            print("Create button clicked successfully")
        except Exception as e:
            print("Create button not clickable within the specified time:", e)

    def click_on_group_delete_button(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.GROUP_DELETE_BUTTON).click()
            print("Group delete button clicked successfully")
        except Exception as e:
            print("Group delete button not clickable within the specified time:", e)

    def click_on_group_delete_approve_button(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.APPROVE_BUTTON).click()
            print("Approve button clicked successfully")
        except Exception as e:
            print("Approve button not clickable within the specified time:", e)

    def click_on_group_delete_decline_button(self):
        try:
            self.driver.implicitly_wait(5)
            wait_until_visible(self, GroupPage.DECLINE_BUTTON).click()
            print("Decline button clicked successfully")
        except Exception as e:
            print("Decline button not clickable within the specified time:", e)

    def toster(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.presence_of_element_located(self.TOASTER)).text
        print("Toaster message: " + title)
        return title

    # def checkbox_click(self, index_list):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.SELECT_LIST))
    #         elements = self.driver.find_elements(*self.SELECT_LIST)
    #         for i in index_list:
    #             elements[i].click()
    #         print(" Selected successfully")
    #     except Exception as e:
    #         print(" Unable to select within the specified time:", e)
    #
    #
    # def click_on_assistant_select(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.ASSISTANT_SELECT)).click()
    #         print(" Clicked on assistant select successfully")
    #     except Exception as e:
    #         print(" Assistant select not clickable within the specified time:", e)
    #
    # def click_on_level_select(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.LEVEL_SELECT)).click()
    #         print(" Clicked on level select successfully")
    #     except Exception as e:
    #         print(" Level select not clickable within the specified time:", e)
    #
    # def click_on_trainer_select(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.TRAINER_SELECT)).click()
    #         print(" Clicked on trainer select successfully")
    #     except Exception as e:
    #         print(" Trainer select not clickable within the specified time:", e)
    #
    # def click_on_sport_type_select(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.SPORT_TYPE_SELECT)).click()
    #         print(" Clicked on sport type select successfully")
    #     except Exception as e:
    #         print(" Sport type select not clickable within the specified time:", e)
    #
    # def select(self, index):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.SELECT_LIST))
    #         self.driver.find_elements(*GroupPage.SELECT_LIST)[index].click()
    #         print(" Selected successfully")
    #     except Exception as e:
    #         print(" Unable to select within the specified time:", e)
    #
    # def click_on_add_group(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.ADD_GROUP_BUTTON)).click()
    #         print(" Clicked on add group button successfully")
    #     except Exception as e:
    #         print(" Add group button not clickable within the specified time:", e)
    #
    # def click_on_groups(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.GROUPS_BUTTON)).click()
    #         print(" Clicked on groups button successfully")
    #     except Exception as e:
    #         print(" Groups button not clickable within the specified time:", e)

    GROUP_PAGE_CREATE_TITLE = (By.CSS_SELECTOR, "form > div:nth-child(1) > p")

    # def enter_group_name(self, group_name):
    #     try:
    #         wait = WebDriverWait(self.driver, 100000)
    #         wait.until(EC.visibility_of_element_located(self.GROUP_NAME_INPUT)).send_keys(group_name)
    #         print(" Group name entered successfully")
    #     except Exception as e:
    #         print(" Group name not entered within the specified time:", e)

    def generate_random_armenian_letters(length):
        armenian_letters = "աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցուփքևօֆԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔԵՎՕՖ"
        return ''.join(random.choice(armenian_letters) for _ in range(length))

    random_armenian_string = generate_random_armenian_letters(8)

    # def toster_wait(self):
    #     wait = WebDriverWait(self.driver, 100000)
    #     title = wait.until(EC.presence_of_element_located(self.TOASTER)).text
    #     print(" Toaster message: " + title)
    #     return title

    def until_document_ready(self, timeout=10):
        def is_document_ready(driver):
            return driver.execute_script("return document.readyState == 'complete'")

        wait = WebDriverWait(self.driver, timeout)
        wait.until(is_document_ready)
