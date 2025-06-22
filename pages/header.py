from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):

    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    ACCOUNT_ICON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

    def product_search(self, search_input):
        self.input_text(search_input, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(10)

    def cart_icon(self):
        # self.click(*self.CART_ICON)
        self.wait_for_element_click(*self.CART_ICON)
        sleep(2)

    def account_icon(self):
        self.wait_for_element_click(*self.ACCOUNT_ICON)

    def search_icon(self):
        self.wait_for_element_click(*self.SEARCH_ICON)