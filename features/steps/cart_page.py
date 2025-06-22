from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when( 'Open cart url' )
def open_target(context):
    context.driver.get('https://www.target.com/cart')


@then( 'Verify message Your cart is empty is displayed' )
def verify_message(context):
    # expected_text = 'Your cart is empty'
    # actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    # assert expected_text in actual_text, \
    #     f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"
    context.app.cart_page.verify_empty_cart_message()


@then( 'Verify Cart Page opened' )
def verify_cart_page(context):
    context.app.cart_page.verify_cart_opened()


@then( 'Verify cart has {expected_quantity} item(s)' )
def verify_quantity(context, expected_quantity):
    context.app.cart_page.verify_quantity('1')


@then( 'Verify cart has correct {product}' )
def verify_product_in_cart(context, product):
    # product_name_in_cart = context.driver.find_element(*PRODUCT_NAME_IN_CART).text
    # print('Name in cart: ', product_name_in_cart)
    #
    # assert 'Hat' or 'hat' in product_name_in_cart, \
    #     f'Expected {context.product_name} did not match {product_name_in_cart}'
    context.app.cart_page.store_product_name_in_cart()
