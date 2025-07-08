from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class HelpPage(Page):

    SELECT_DD = (By.CSS_SELECTOR, "[id*='viewHelpTopics:ViewHelpTopics']")


    def open_returns_exchanges_page(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_promotions_dd(self, value):
        dd = self.find_element(*self.SELECT_DD)
        select = Select(dd)
        select.select_by_visible_text(value)

    def verify_returns_exchanges_page(self):
        self.verify_partial_url('Returns')

    def verify_help_current_promotions_page(self):
        self.verify_partial_url('Current+promotions')