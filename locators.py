from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.XPATH, '//input[@id="email"]')
PASSWORD_FIELD = (By.XPATH, '//input[@id="current-password"]')
CATALOG_SECTION = (By.XPATH, '//*[contains(text(), "Диалог")]')
SEARCH_FIELD = (By.XPATH, '//textarea')
ANSWER_AREA = (By.XPATH, '//*[contains(text(), "КоАП РФ")]')
