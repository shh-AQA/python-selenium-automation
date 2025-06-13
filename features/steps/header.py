from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when( 'User clicks on shopping cart icon' )
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@when('User click on Account icon')
def click_account_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(1)

@when( 'Input {product} into search field' )
def input_product(context, product):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product)
    sleep(1)

@when( 'Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By. CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(1)

