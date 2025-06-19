from pyexpat.errors import messages

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.XPATH, "//*[contains(@id, 'addToCartButtonOrTextIdFor')]")
CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
PRODUCT_NAME = (By.ID, 'pdp-product-title-id')
PRODUCT_IMG = (By.CSS_SELECTOR, "[data-test*='@web/ProductCard/ProductCardImage/primary']")
PRODUCT_CARD = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@when( 'Click on Add to Cart')
def click_on_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_NAME)).text
    print(f"Product Name: {context.product_name}")


@when( 'Click on product image' )
def click_product_image(context):
    # context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_IMG)).click()
    context.driver.find_element(*PRODUCT_IMG).click()
    sleep(2)


@then( 'Verify message Your cart is empty is displayed' )
def verify_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"

@then( 'Verify every product has a name and image' )
def verify_every_product_name_img(context):
    products = context.driver.find_elements(*PRODUCT_CARD)[:4]
    print(f"Found {len(products)} products")


    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        img = product.find_element(*PRODUCT_IMG)
        assert img, 'No image displayed'


