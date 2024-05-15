from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://dev.sport.yerevan.am/login")

    def is_loaded(self):
        return "Մարզադպրոցների կառավարման համակարգ" in self.driver.title

    USERNAME_FIELD = (By.CSS_SELECTOR, "div:nth-child(1) > div > input[type=text]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "div:nth-child(2) > div > input[type=password]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "form > button")

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    def contains_text(self, text):
        return text in self.driver.page_source
