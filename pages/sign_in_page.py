from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    sign_in_create_account_txt = 'Sign in or create account'

    SIGN_IN_TXT = (By.XPATH, "//h1[text()='Sign in or create account']")
    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_tc_link(self):
        self.click(*self.TERMS_AND_CONDITIONS_LINK)

    def verify_sign_in_create_account_form(self):
        self.verify_text(self.sign_in_create_account_txt, *self.SIGN_IN_TXT)