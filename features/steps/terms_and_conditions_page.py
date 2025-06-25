from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Terms and Conditions page is opened')
def verify_privacy_page_opened(context):
    context.app.terms_and_conditions_page.verify_tc_page_opened()

@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)