from selenium.webdriver.common.actions.action_builder import ActionBuilder

from time import sleep

from pages.login_page import LoginPage
from constants import USER_EMAIL, USER_PASSWD


def fill_login_form(driver):
    counter = 0
    login_page = LoginPage(driver)
    while not login_page.email_ready() and counter <= 60:
        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(700, 348)
        action.pointer_action.click()
        action.perform()
        counter += 1
        sleep(1)

    login_page.email_field().send_keys(USER_EMAIL)

    action = ActionBuilder(driver)
    action.pointer_action.move_to_location(700, 410)
    action.pointer_action.click()
    action.perform()
    login_page.password_field().send_keys(USER_PASSWD)

    action.pointer_action.move_to_location(700, 470)
    action.pointer_action.click()
    action.perform()