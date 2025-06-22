from pages.base_page import Page
from pages.cart_overlay import CartOverlay
from pages.cart_page import CartPage
from pages.header import Header
from pages.login_overlay import LoginModal
from pages.main_page import MainPage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.cart_page = CartPage(driver)
        self.cart_overlay = CartOverlay(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.login_modal = LoginModal(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)


