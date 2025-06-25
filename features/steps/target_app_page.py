from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app_page()


@given('Store original window')
def get_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()
    ##stores and prints ID of original window, get method from base_page


@when('Click on Privacy Policy link')
def click_privacy_policy(context):
    context.app.target_app_page.click_privacy_policy()


@when('Switch to new window')
def switch_window(context):
    # sleep(2)
    # all_windows = context.driver.window_handles #stores ID's for all windows in a list
    # print(context.driver.window_handles) ##prints all window handles after privacy policy link is clicked
    # print('Current window ID: ', context.driver.current_window_handle)
    #
    # context.driver.switch_to.window(context.driver.window_handles[1])
    # print('Switched to window ID: ', context.driver.current_window_handle)
    ###SELENIUM####
    context.app.target_app_page.switch_to_new_window()


@then('Verify Privacy Page opened')
def verify_privacy_page_opened(context):
    context.app.privacy_policy_page.verify_pp_page_opened()

@then('Close current window')
def close_current_window(context):
    context.app.base_page.close_window() #linked to base_page, step can be reused

@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)

