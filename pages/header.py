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