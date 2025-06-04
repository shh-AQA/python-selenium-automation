from selenium.webdriver.common.by import By
from behave import given, when, then


@given( 'Open target main page' )
def open_target(context):
    context.driver.get('https://www.target.com/')

@when( 'User clicks on shopping cart icon' )
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then( 'Verify message Your cart is empty is displayed' )
def verify_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"