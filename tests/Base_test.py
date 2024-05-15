import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest


class Before(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def setUp(self):
        try:
            self.driver.maximize_window()
            self.driver.get("http://dev.sport.yerevan.am/")
            print("\nPage loaded successfully")
            try:
                login_button = self.driver.find_element(By.CSS_SELECTOR, "div > button.button-container")
                login_button.click()
                username_input = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > input[type=text]")
                username_input.send_keys("Jinanyan")
                password_input = self.driver.find_element(By.CSS_SELECTOR,
                                                          "div:nth-child(2) > div > input[type=password]")
                password_input.send_keys("Jinanyan*11")
                submit_login = self.driver.find_element(By.CSS_SELECTOR, "form > button")
                submit_login.click()
                print("Logged in successfully")
            except Exception as e:
                print("Could not login:", e)
        except Exception as e:
            print("\nCould not load page:", e)

    def tearDown(self):
        try:
            arrow = self.driver.find_element(By.CSS_SELECTOR, "div.user_container > svg")
            arrow.click()
            self.driver.implicitly_wait(5)
            logout_button = self.driver.find_element(By.CSS_SELECTOR, "div.logout-section.section-open > div")
            logout_button.click()
            print("Logged out successfully")
        except Exception as e:
            print("Could not log out successfully", e)
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
