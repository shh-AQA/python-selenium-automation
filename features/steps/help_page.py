from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HELP_HEADER = (By.CSS_SELECTOR, "h2.custom-h2")
SEARCH_INPUT_FIELD = (By.ID, 'j_id0:j_id2:j_id44:name')
SEARCH_BTN = (By.CSS_SELECTOR, '.btn-sm.search-btn')
WHAT_WOULD_YOU_LIKE_TO_DO = (By.XPATH, "//*[contains(@class, 'container')]//*[@class='col-lg-12']")
CONTACT_US_AND_PRODUCT_RECALLS = (By.XPATH, "//*[contains(@class, 'container')]//*[@class='col-lg-12']")
BROWSE_ALL_HELP_TEXT = (By.XPATH, "//h2[text()='Browse all Help pages']")

@given( 'Open Target Help page' )
def open_target(context):
    context.driver.get('https://help.target.com/help')

@given('Open Help Page for returns')
def open_returns_and_exchanges_page(context):
    context.app.help_page.open_returns_exchanges_page()

@when('Select help topic {value}')
def select_promotions_dd(context, value):
    context.app.help_page.select_promotions_dd(value)

@then('Verify help returns page opened')
def verify_help_page(context):
    context.app.help_page.verify_returns_exchanges_page()

@then('Verify help current promotions page opened')
def verify_help_current_promotions_page(context):
    context.app.help_page.verify_help_current_promotions_page()

@then( 'Verify Target Help header' )
def verify_help_header(context):
    context.driver.find_element(*HELP_HEADER)

@then( 'Verify search help input field' )
def verify_search_help_input(context):
    context.driver.find_element(*SEARCH_INPUT_FIELD)

@then( 'Verify search button' )
def verify_search_button(context):
    context.driver.find_element(*SEARCH_BTN)

@then( 'Verify What would you like to do section' )
def verify_what_to_do_section(context):
    context.driver.find_element(*WHAT_WOULD_YOU_LIKE_TO_DO)

@then( 'Verify contact us and product recalls section' )
def verify_what_to_do_section(context):
    context.driver.find_elements(*CONTACT_US_AND_PRODUCT_RECALLS)

@then( 'Verify Browse all help pages text is displayed' )
def verify_browse_all_help_pages(context):
    context.driver.find_element(*BROWSE_ALL_HELP_TEXT)
