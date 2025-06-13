from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when( 'Click on Add to Cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor81304692').click()
    sleep(1)


@then( 'Verify message Your cart is empty is displayed' )
def verify_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"
