import random
import re

class BasePage:
    def __init__(self, driver):
        self.driver = driver


class RandomNumberGenerator:
    @staticmethod
    def generate_random_numbers():
        random_numbers = []
        for _ in range(8):
            number = "44" + "".join(str(random.randint(0, 9)) for _ in range(6))
            random_numbers.append(number)
        return random_numbers


def validate_password(password):
    if len(password) < 8:
        return False

    contains_uppercase = re.search(r'[Ա-Ֆ]', password)
    contains_lowercase = re.search(r'[ա-ֆ]', password)
    contains_digit = re.search(r'\d', password)
    contains_special = re.search(r'[!@#$%^&*()_=+]', password)

    if not (contains_uppercase and contains_lowercase and contains_digit and contains_special):
        return False

    return True
