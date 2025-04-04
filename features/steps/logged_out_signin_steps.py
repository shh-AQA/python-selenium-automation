from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def sign_in_after_logged_out(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']").click()
    sleep(2)

@when('From right side navigation menu, click Sign In')
def click_sign_in_menu(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_signin_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    expected_text = 'Sign in or create account'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'