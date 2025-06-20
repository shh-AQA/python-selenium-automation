from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductListPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search(self, *locator):
        expected_text = 'shoes'
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'shoes' in actual_text, f'Error. Expected Text: \'shoes\' not in {actual_text}'