from selenium.webdriver.common.by import By


class OnlinePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://dev.sport.yerevan.am/phone-verification")

    def is_loaded(self):
        return "Առցանց դիմում" in self.driver.page_source

    PHONE_NUMBER_INPUT_FIELD = (By.CSS_SELECTOR, "input[type=tel]")
    GET_CODE_BUTTON = (By.CSS_SELECTOR, "form > button")
    PIN_INPUT_FIELD = (By.CSS_SELECTOR, "input[type=text]")
    NEW_PIN_BUTTON = (By.CSS_SELECTOR, "form > button:nth-child(3)")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "form > button:nth-child(4)")
    SSN_INPUT_FIELD = (By.CSS_SELECTOR, "div:nth-child(1) > div > div > input[type=text]")
    DATEPICKER_INPUT_FIELD = (By.CSS_SELECTOR, "div.child-registration_date-input > div > div > input[type=text]")
    SPORT_SCHOOL_SELECT = (By.CSS_SELECTOR, "form > div:nth-child(2) > div > div > div")
    SPORT_SCHOOLS = (By.CSS_SELECTOR, "form > div:nth-child(2) > div > div > div:nth-child(2) > div > div")
    SPORT_TYPE_SELECT = (By.CSS_SELECTOR, "form > div:nth-child(3) > div > div > div")
    SPORT_TYPES = (By.CSS_SELECTOR, "form > div:nth-child(3) > div > div > div:nth-child(2) > div > div")
    CHECKBOX = (By.CSS_SELECTOR, "#scales")
    CHECK_BUTTON = (By.CSS_SELECTOR, "form > button")
    APP_CONFIRM_BUTTON = (By.CSS_SELECTOR, "form > button")
    FINAL_CONFIRM_BUTTON = (By.CSS_SELECTOR, "form > button")

    def new_pin_button(self):
        button = self.driver.find_element(*OnlinePage.NEW_PIN_BUTTON)
        return button.is_enabled()

    def click_on_app_confirm_button(self):
        self.driver.find_element(*OnlinePage.APP_CONFIRM_BUTTON).click()

    def click_on_check_button(self):
        self.driver.find_element(*OnlinePage.CHECK_BUTTON).click()

    def click_on_checkbox(self):
        self.driver.find_element(*OnlinePage.CHECKBOX).click()

    def select_sport_type(self, index):
        self.driver.find_elements(*OnlinePage.SPORT_TYPES)[index].click()

    def click_on_sport_type_select(self):
        self.driver.find_element(*OnlinePage.SPORT_TYPE_SELECT).click()

    def select_sport_school(self, index):
        self.driver.find_elements(*OnlinePage.SPORT_SCHOOLS)[index].click()

    # def click_on_first_sport_school(self):
    #     self.driver.find_elements(*OnlinePage.SPORT_SCHOOLS)[3].click()

    def click_get_code_button(self):
        self.driver.find_element(*OnlinePage.GET_CODE_BUTTON).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*OnlinePage.PHONE_NUMBER_INPUT_FIELD).send_keys(phone_number)

    def enter_pin(self, pin):
        self.driver.find_element(*OnlinePage.PIN_INPUT_FIELD).send_keys(pin)

    def click_confirm_button(self):
        self.driver.find_element(*OnlinePage.CONFIRM_BUTTON).click()

    def enter_ssn(self, ssn):
        self.driver.find_element(*OnlinePage.SSN_INPUT_FIELD).send_keys(ssn)

    def enter_date(self, date):
        self.driver.find_element(*OnlinePage.DATEPICKER_INPUT_FIELD).send_keys(date)

    def click_on_school_select(self):
        self.driver.find_element(*OnlinePage.SPORT_SCHOOL_SELECT).click()
