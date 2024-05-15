from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelpers:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def until(self, condition):
        return self.wait.until(condition)

    # def wait_until_visible(self, locator):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located(locator))


def wait_until_clickable(self, locator):
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.element_to_be_clickable(locator))


def wait_until_visible(self, locator, timeout=10):
    return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_until_intractable(self, locator, timeout=10):
    return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_until_selected(self, locator, timeout=10):
    return WebDriverWait(self.driver, timeout).until(
        EC.element_located_selection_state_to_be(locator, True)
    )

# def wait_until_page_fully_loaded(self, locator, timeout=30):
#     try:
#         WebDriverWait(self.driver, timeout).until(
#             EC.presence_of_element_located(locator)  # Wait until the body tag is present
#         )
#         WebDriverWait(self.driver, timeout).until(
#             EC.visibility_of_element_located(locator)  # Wait until the body tag is visible
#         )
#         print("Page is fully loaded")
#     except Exception as e:
#         print("Timed out waiting for page to be fully loaded:", e)


# def wait_until_all_elements_present(self, locator, timeout=50):
#     try:
#         WebDriverWait(self.driver, timeout).until(
#             EC.presence_of_all_elements_located(locator)
#         )
#         print(f"All elements located by {locator} are present in the DOM")
#     except Exception as e:
#         print(f"Timed out waiting for all elements located by {locator} to be present in the DOM:", e)


# def wait_until_element_visible(self, locator, timeout=30, retry_attempts=5):
#     for _ in range(retry_attempts):
#         try:
#             WebDriverWait(self.driver, timeout).until(
#                 EC.visibility_of_element_located(locator)
#             )
#             return True  # Element is visible
#         except TimeoutException:
#             continue  # Retry if TimeoutException occurs
#     return False  # Element is not visible after retry attempts
