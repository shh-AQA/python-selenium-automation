from selenium.webdriver.common.by import By
from pages.base_page import Page

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartOverlay(Page):

    VIEW_CART_AND_CHECKOUT_BTN = (By.XPATH, "//a[contains(text(),'View cart')]")

    def click_cart_checkout_btn(self):
        self.wait_for_element_click(*self.VIEW_CART_AND_CHECKOUT_BTN)



