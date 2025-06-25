from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('Store original window')
def get_original_window(context):
    context.original_window = context.app.base_page.get_current_window_id()
    ##stores and prints ID of original window, get method from base_page

@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_tc_link()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()



@then( 'Verify sign in form is displayed')
def verify_sign_in_create_account_form(context):
    # expected_text = 'Sign in or create account'
    # actual_text = context.driver.find_element(*SIGN_IN_TXT).text
    # assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"

     context.app.sign_in_page.verify_sign_in_create_account_form()