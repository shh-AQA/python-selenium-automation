from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given( 'Open target circle page' )
def open_target(context):
    context.driver.get('https://www.target.com/circle')

@then( 'Verify at least {number} benefit cells are displayed')
def verify_benefit_cells(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")

    assert len(links) >= int(number), f"Expected at least 10 links, got {len(links)}"