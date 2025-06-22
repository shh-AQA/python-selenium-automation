from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_SIDE_NAV = (By.CSS_SELECTOR,"[data-test*='orderPickupButton']")

@when('Click on Add to Cart in side navigation')
def click_cart_button(context):
    context.driver.wait.until(
            EC.visibility_of_element_located(ADD_TO_CART_SIDE_NAV),
            message='Product name was not visible'
        ).click()

