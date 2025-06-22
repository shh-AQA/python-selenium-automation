from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CartPage(Page):
    cart_empty_txt = 'Your cart is empty'

    #locators:
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_empty_cart_message(self):
        self.verify_text(self.cart_empty_txt, *self.CART_EMPTY_MSG)

    def verify_cart_opened(self):
        # self.verify_url('https://www.target.com/cart')
        self.verify_partial_url('/cart')

    def verify_quantity(self, expected_quantity):
        self.verify_partial_text(expected_quantity, *self.CART_SUMMARY)

    def store_product_name_in_cart(self):
        product = self.find_element(*self.PRODUCT_NAME_IN_CART)