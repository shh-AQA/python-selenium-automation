from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

# init driver
# 3 A's: Arrange
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')



#Create locators + search strategy for page elements of Amazon Sign in page

# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'signin_notification_condition_of_use')]")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'signin_notification_privacy_notice')]")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
