from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

@when( 'User clicks on Sign in or create account button in login modal' )
def sign_in_create_account_btn(context):
    # context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), message="Element not clickable").click()
    # sleep(1)

    context.app.login_modal.sign_in_create_account_btn()
