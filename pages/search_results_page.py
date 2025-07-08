from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page



class SearchResultsPage(Page):


    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[data-test*='@web/ProductCard/ProductCardImage/primary']")
    FAV_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TT_TXT = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")


    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TXT)
        # expected_text = 'shoes'
        # actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        # assert 'shoes' in actual_text, f'Error. Expected Text: \'shoes\' not in {actual_text}'

    def click_on_product_img(self):
        self.wait_for_element_click(*self.PRODUCT_IMG)


    def hover_favorites_icon(self):
        self.hover_element(*self.FAV_ICON)


    def verify_tooltip_is_displayed(self):
        self.wait_for_element(*self.FAV_TT_TXT)
