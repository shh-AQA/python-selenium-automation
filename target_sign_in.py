from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')



#Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)
#
# Test Case: Users can navigate to SignIn page
# 1. Open https://www.target.com/
# 2. Click Account button
driver.find_element(By.ID, 'account-sign-in').click()


# 3. Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# 4. Verify SignIn page opened:
# “Sign in or create account” text is shown,
driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")

# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.XPATH, "//button[contains(@class, 'styles_ndsBaseButton__W8Gl7 styles_lg___H2I') and @type='button']")