from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@then( 'Verify sign in form is displayed')
def verify_sign_in_create_account_form(context):
    # expected_text = 'Sign in or create account'
    # actual_text = context.driver.find_element(*SIGN_IN_TXT).text
    # assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"

     context.app.sign_in_page.verify_sign_in_create_account_form()