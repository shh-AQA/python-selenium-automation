from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    sign_in_create_account_txt = 'Sign in or create account'

    SIGN_IN_TXT = (By.XPATH, "//h1[text()='Sign in or create account']")

    def verify_sign_in_create_account_form(self):
        self.verify_text(self.sign_in_create_account_txt, *self.SIGN_IN_TXT)