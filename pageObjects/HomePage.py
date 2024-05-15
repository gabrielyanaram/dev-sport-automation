class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://dev.sport.yerevan.am/")

    def contains_text(self, text):
        return text in self.driver.page_source
