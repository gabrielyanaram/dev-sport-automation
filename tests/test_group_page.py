import time
import pytest
from selenium import webdriver
from pageObjects.GroupPage import GroupPage
from tests.Base_test import Before
import sys

sys.path.append('/PycharmProjects/pythonProject5')


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


random_armenian_string = GroupPage.generate_random_armenian_letters(8)


# def test_group_page_load(browser):
#     before = Before(browser)
#     before.setUp()
#     time.sleep(2)
#     group_page = GroupPage(browser)
#     time.sleep(2)
#     group_page.load()
#     time.sleep(2)
#     assert group_page.is_loaded()
#     time.sleep(2)
#     before.tearDown()

def test_group_create(browser):
    before = Before(browser)
    before.setUp()
    group_page = GroupPage(browser)
    group_page.click_on_groups()
    group_page.click_on_add_group()
    group_page.enter_group_name(random_armenian_string)
    group_page.click_on_sport_type_select()
    group_page.select(0)
    group_page.click_on_trainer_select()
    group_page.checkbox_click([0, -1])
    group_page.click_on_trainer_select()
    group_page.click_on_level_select()
    group_page.checkbox_click([0, -1])
    group_page.click_on_level_select()
    group_page.click_on_assistant_select()
    group_page.checkbox_click([0, -1])
    group_page.click_on_assistant_select()
    group_page.click_on_create_button()
    assert group_page.toster() in "ՀԱՋՈՂՎԱԾ"
    before.tearDown()
    # group_page.find_and_click_on_group_with_name(random_armenian_string)
    time.sleep(1)


def test_single_group(browser):
    group_page = GroupPage(browser)
    group_page.click_on_groups()
    group_page.find_and_click_on_group_with_name(random_armenian_string)
    group_page.click_on_group_delete_button()
    group_page.click_on_group_delete_decline_button()
    group_page.click_on_group_delete_button()
    group_page.click_on_group_delete_approve_button()
    assert group_page.toster() in "ՀԱՋՈՂՎԱԾ"
    time.sleep(3)
