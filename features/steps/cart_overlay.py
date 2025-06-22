from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when( 'User clicks on shopping cart icon in cart overlay' )
def click_cart_checkout_btn(context):
    context.app.cart_overlay.click_cart_checkout_btn()