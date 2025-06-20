from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ACCOUNT_ICON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_ICON = (By. CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

@when( 'User clicks on shopping cart icon' )
def cart_icon(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.cart_icon()



@when('User click on Account icon')
def click_account_icon(context):
    context.driver.find_element(*ACCOUNT_ICON).click()
    # sleep(1)

@when( 'Input {product} into search field' )
def input_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_ICON).click()
    # sleep(10)
    context.app.header.product_search()

@when( 'Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(2)

