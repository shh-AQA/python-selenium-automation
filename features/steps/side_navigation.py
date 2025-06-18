from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
ADD_TO_CART_SIDE_NAV = (By.CSS_SELECTOR,"[data-test*='orderPickupButton']")
ADD_TO_CART_TXT = (By.XPATH, "//span[text()='Added to cart']")
VIEW_CART_AND_CHECKOUT_BTN = (By.XPATH, "//a[text()='View cart & check out']")


@when( 'User clicks on Sign in or create account button in side navigation' )
def click_sign_in_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), message="Element not clickable").click()
    # sleep(1)

@when('Click on Add to Cart in side navigation')
def click_cart_button(context):
    context.driver.wait.until(
            EC.visibility_of_element_located(ADD_TO_CART_SIDE_NAV),
            message='Product name was not visible'
        ).click()

@when( "Click on 'View Cart & checkout' button in side navigation" )
def click_view_cart_button(context):
    context.driver.find_element(*VIEW_CART_AND_CHECKOUT_BTN).click()

#
# @then( 'Verify product is added to shopping cart' )
# def verify_product(context):
#     text = context.driver.find_element(*ADD_TO_CART_TXT).text
#     assert text == 'Added to cart', f"{text} != Added to cart"