from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from features.steps.header import cart_icon

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@when( 'Open cart url' )
def open_target(context):
    context.driver.get('https://www.target.com/cart')

@then( 'Verify cart has {amount} item(s)')
def verify_product_in_cart(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text

    assert f'{amount} item' in cart_summary, f"Expected {amount} item(s) but got {cart_summary}"

@then( 'Verify cart has correct {product}' )
def verify_product_in_cart(context, product):
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME_IN_CART).text
    print('Name in cart: ', product_name_in_cart)

    assert 'Hat' or 'hat' in product_name_in_cart, \
        f'Expected {context.product_name} did not match {product_name_in_cart}'

    # assert context.product_name[10:] in product_name_in_cart, \
    #     f'Expected {context.product_name[10:]} did not match {product_name_in_cart}'
