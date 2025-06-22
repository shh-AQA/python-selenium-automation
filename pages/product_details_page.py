from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


# noinspection PyStatementEffect
class ProductDetailsPage(Page):


    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton']")


    def store_product_name_details_page(self):
        product_name = self.wait_for_element(*self.PRODUCT_TITLE).text
        print(f"Product name: {product_name}")
        return product_name


    def product_details_page_add_to_cart_btn(self):
        sleep(4)
        self.wait_for_element_click(*self. ADD_TO_CART_BTN)