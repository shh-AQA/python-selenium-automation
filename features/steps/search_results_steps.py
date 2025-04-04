from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_RESULT = (By.XPATH, "//div[@data-test='lp-resultsCount']")


@then("Verify search results are shown and include {expected_result}")
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result in actual_result, f'Error. Text {expected_result} not in {actual_result}'