import logging

from constants import REFERENCE_TEXT
from pages.login_page import LoginPage
from pages.dialog_page import DialogPage
from tests_functions.login import fill_login_form
from tests_functions.catalog import catalog_select
from tests_functions.dialog import search_action

logger = logging.getLogger(__name__)


def test_dialog(driver):
    logger.info("Тест запущен - OK!")
    login_page = LoginPage(driver)
    login_page.load()

    fill_login_form(driver)

    # TO DO: проверить, что авторизация успешна

    catalog_select(driver)

    # TO DO: проверить, что раздел ДИАЛОГ открыт

    search_action(driver)

    dialog_page = DialogPage(driver)
    text = dialog_page.answer_text()
    logger.info(f"Текст получен - {text}")
    assert text == REFERENCE_TEXT, 'Полученный текст не совпадает с эталонным - ERROR!'
