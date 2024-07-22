from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from time import sleep

from pages.dialog_page import DialogPage
from constants import TEST_PHRASE


def search_action(driver):
    action = ActionBuilder(driver)
    action.pointer_action.move_to_location(390, 630)
    action.pointer_action.click()
    action.perform()

    dialog_page = DialogPage(driver)
    dialog_page.search_field().send_keys(TEST_PHRASE)
    dialog_page.search_field().send_keys(Keys.RETURN)

def get_answer(driver):
    counter = 0

    while not dialog_page.answer_ready() and counter <= 60:
        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(328, 208)
        action.pointer_action.click()
        action.perform()
        counter += 1
        sleep(1)

    dialog_page = DialogPage(driver)
    dialog_page.search_field().send_keys(TEST_PHRASE)