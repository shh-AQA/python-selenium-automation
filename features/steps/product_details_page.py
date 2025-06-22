from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-94268550 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/women-s-smocked-v-waist-midi-dress-a-new-day/-/A-94268550?preselect=94191336#lnk=sametab')
    sleep(8)

@when( 'Click on Add to Cart on product details page' )
def click_on_cart(context):
    # context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
    context.app.product_details_page.product_details_page_add_to_cart_btn()


@when( 'Store product name from product details page' )
@when("Store product name from product details page")
def store_product_name(context):
    context.product_name = context.app.product_details_page.store_product_name_details_page()


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Cream Seashell', 'Navy Blue', 'Yellow Gingham']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'




