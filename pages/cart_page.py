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
