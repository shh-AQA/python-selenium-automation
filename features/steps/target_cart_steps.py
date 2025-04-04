from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then


EMPTY_CART = (By.XPATH, "//h1[text()='Your cart is empty']")


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context):
    actual_text = context.driver.find_element(*EMPTY_CART).text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'