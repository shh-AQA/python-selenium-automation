from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given( 'Open Target Help page' )
def open_target(context):
    context.driver.get('https://help.target.com/help')

@then( 'Verify Target Help header' )
def verify_help_header(context):
    context.driver.find_element(By.CSS_SELECTOR, "h2.custom-h2")

@then( 'Verify search help input field' )
def verify_search_help_input(context):
    context.driver.find_element(By.ID, 'j_id0:j_id2:j_id44:name')

@then( 'Verify search button' )
def verify_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '.btn-sm.search-btn')

@then( 'Verify What would you like to do section' )
def verify_what_to_do_section(context):
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'container')]//*[@class='col-lg-12']")

@then( 'Verify contact us and product recalls section' )
def verify_what_to_do_section(context):
    context.driver.find_elements(By.XPATH, "//*[contains(@class, 'container')]//*[@class='col-lg-12']")

@then( 'Verify Browse all help pages text is displayed' )
def verify_browse_all_help_pages(context):
    context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")
