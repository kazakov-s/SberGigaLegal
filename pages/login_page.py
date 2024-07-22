from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from constants import TEST_URL
from locators import EMAIL_FIELD, PASSWORD_FIELD


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(TEST_URL)

    def email_field(self):
        return WebDriverWait(self.browser, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(EMAIL_FIELD)
        )

    def email_ready(self):
        try:
            WebDriverWait(self.browser, timeout=10).until(EC.element_to_be_clickable(EMAIL_FIELD))
            return True
        except Exception:
            return False

    def password_field(self):
        return WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable(PASSWORD_FIELD)
        )

    def enter_btn(self):
        pass
