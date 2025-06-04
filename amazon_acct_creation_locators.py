from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

# init driver
# 3 A's: Arrange
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Find the most optimal locators for Create Account on amazon.com (Registration) page elements:

#Amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo") #by class

#Create account text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small") #by tag + class

#Your name field
driver.find_element(By. ID, 'ap_customer_name')

#Email field
driver.find_element(By. ID, 'ap_email')

#Password field
driver.find_element(By.ID, 'ap_password')

#Password info
driver.find_element(By.ID, 'auth-password-requirement-info')

#Re-Enter password field
driver.find_element(By.ID, 'ap_password_check')

#Create Amazon account or Continue button
driver.find_element(By.ID, 'continue')

#Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "[href*='help/customer/display.html/ref=continue']") #by attribute with partial match

#Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']") #by attribute with partial match

#Sign in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis") #by class