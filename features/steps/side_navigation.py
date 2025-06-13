from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when( 'User clicks on Sign in or create account button in side navigation' )
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(1)

@when('Click on Add to Cart in side navigation')
def click_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test*='orderPickupButton']" ).click()
    sleep(5)

@then( 'Verify product is added to shopping cart' )
def verify_product(context):
    text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']").text
    assert text == 'Added to cart', f"{text} != Added to cart"