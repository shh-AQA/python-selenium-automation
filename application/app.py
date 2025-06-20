from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.product_list_page import ProductListPage



class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.product_list_page = ProductListPage(driver)
        self.cart_page = CartPage(driver)
