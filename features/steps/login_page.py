from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then( 'Verify sign in form is displayed')
def verify_sign_in(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"