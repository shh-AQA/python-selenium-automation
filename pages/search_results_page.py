from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):


    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[data-test*='@web/ProductCard/ProductCardImage/primary']")


    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TXT)
        # expected_text = 'shoes'
        # actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        # assert 'shoes' in actual_text, f'Error. Expected Text: \'shoes\' not in {actual_text}'

    def click_on_product_img(self):
        self.wait_for_element_click(*self.PRODUCT_IMG)

    # noinspection PyStatementEffect
    def store_product_name(self, product):
        self.wait_for_element(*self.PRODUCT_TITLE).text
        print(f"Product name stored: {product}")