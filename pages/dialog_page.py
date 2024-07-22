from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from locators import SEARCH_FIELD, ANSWER_AREA, EMAIL_FIELD


class DialogPage:
    def __init__(self, browser):
        self.browser = browser

    def search_field(self):
        return WebDriverWait(self.browser, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(SEARCH_FIELD)
        )

    def answer_ready(self):
        try:
            WebDriverWait(self.browser, timeout=120).until(EC.element_to_be_clickable(EMAIL_FIELD))
            return True
        except Exception:
            return False

    def answer_text(self):
        text = WebDriverWait(self.browser, timeout=60, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(ANSWER_AREA)
        ).text

        full_text = f'Согласно статье статье 6.24 {text}'
        return full_text