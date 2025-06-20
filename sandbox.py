########## HEADER PAGE######

from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def product_search(self):
        self.input_text('shoes', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(10)

    def cart_icon(self):
        self.click(*self. CART_ICON)
        sleep(2)

#########CART PAGE########

from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_empty_cart_message(self):
        expected_text = 'Your cart is empty'
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text in actual_text, \
            f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"


##########HEADER STEPS########

@when( 'User clicks on shopping cart icon' )
def cart_icon(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click()


########CART STEPS#########

@then( 'Verify message Your cart is empty is displayed' )
def verify_message(context):
    # expected_text = 'Your cart is empty'
    # actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    # assert expected_text in actual_text, \
    #     f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"
    context.app.cart_page.verify_empty_cart_message()