from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when("User searches for product {search_word}")
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


@when('User clicks on shopping cart icon')
def shopping_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(2)
