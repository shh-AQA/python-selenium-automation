from selenium.webdriver.common.by import By
from pages.base_page import Page

class PrivacyPolicyPage(Page):

    def verify_pp_page_opened(self):
        self.wait_for_url_contains('target-privacy-policy')

