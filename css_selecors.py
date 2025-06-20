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


#if element has an ID, use By ID
driver.find_element(By.ID, 'twotabsearchtextbox') ### OR ###

#CSS_Selector by ID
driver.find_element(By.CLASS_NAME, '#twotabsearchtextbox') #use the hashtag for CSS by ID

#CSS_Selector by tag + ID
driver.find_element(By.CLASS_NAME, 'input#twotabsearchtextbox') #not used frequently, just an ex of how it can be done

#By one class
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag')

#By more than one class, order doesn't matter
driver.find_element(By.CSS_SELECTOR, 'icp-nav-flag icp-nav-flag-us icp-nav-flag-lop') #place a period b/t each class

#By tag and class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')

#By tag, ID + class. Best practice is to put it in that same order but it will locate anyway
driver.find_element(By.CSS_SELECTOR, 'a#nav-logo-sprites.nav-logo-spritesnav-progressive-attribute')

#By attribute
driver.find_element(By.CSS_SELECTOR, "[href='/ref=nav_logo']")

#By attribute + tag
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=nav_logo']")

#By multiple attributes
driver.find_element(By.CSS_SELECTOR, "[href='/ref=nav_logo'][lang='en']")

#By class + attribute
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=nav_logo']")

#By tag, ID, class and attribute
driver.find_element(By.CSS_SELECTOR, "a#nav-logo-sprites.nav-logo-link[aria-label='Amazon']")

#By attribute, using partial match (*)
driver.find_element(By.CSS_SELECTOR, "[href*='ap_signin_notification_condition_of_use']")

#By class (treat like an attribute) + partial match + multiple classes ****THIS EXAMPLE IS FROM  TARGET****
driver.find_element(By.CSS_SELECTOR, "[class*='tyles_ndsLink'][class*='tyles_onLight'][class*='styles_neverDecorate'][class*='sc-49aad5be-1']")

