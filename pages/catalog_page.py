from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from locators import CATALOG_SECTION


class CatalogPage:
    def __init__(self, browser):
        self.browser = browser

    def catalog_section(self):
        return WebDriverWait(self.browser, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(CATALOG_SECTION)
        )