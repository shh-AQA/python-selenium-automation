from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginModal(Page):

    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


    def sign_in_create_account_btn(self):
        self.wait_for_element_click(*self.SIGN_IN_BTN)