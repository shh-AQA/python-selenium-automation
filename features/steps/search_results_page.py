from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



PRODUCT_CARD = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")


# @when( 'Click on Add to Cart')
# def click_on_cart(context):
    # context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
    # context.app.product_details_page.product_details_page_add_to_cart_btn()


@when('Store product name')
def search_results_product_name(context):
    context.app.product_details_page.store_product_name()
    # context.product_name = context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_TITLE)).text
    # print(f"Product Name: {context.product_name}")


@when('Click on product image')
def click_product_image(context):
    # context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_IMG)).click()
    # context.driver.find_element(*PRODUCT_IMG).click()
    # sleep(2)
    context.app.search_results_page.click_on_product_img()

@when("Hover over 'add to favorites' icon")
def hover_favorites_icon(context):
    context.app.search_results_page.hover_favorites_icon()


@then('Verify search worked for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
    # expected_text = 'shoes'
    # actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    # assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"


@then('Verify every product has a name and image')
def verify_every_product_name_img(context):
    products = context.driver.find_elements(*PRODUCT_CARD)[:4]
    print(f"Found {len(products)} products")

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        img = product.find_element(*PRODUCT_IMG)
        assert img, 'No image displayed'

@then('Verify tooltip is displayed')
def verify_tooltip_is_displayed(context):
    context.app.search_results_page.verify_tooltip_is_displayed()


