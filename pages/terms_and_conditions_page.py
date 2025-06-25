from selenium.webdriver.common.by import By
from pages.base_page import Page

class TermsAndConditionsPage(Page):

        def verify_tc_page_opened(self):
            self.wait_for_url_contains('terms-conditions')