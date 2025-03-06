from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)
#

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Test Case: Users can navigate to SignIn page
# Open https://www.target.com/
driver.get('https://www.target.com/')


# Click SignIn button
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 cOUViz h-margin-r-x3']").click()

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# Verify SignIn page opened:
# “Sign into your Target account” text is shown,
driver.find_element(By.XPATH, "//h1[text() = 'Sign in or create account']")

# SignIn button is shown (you can just use driver.find_element() to check for element’s presence,
# no need to assert here)
driver.find_element(By.ID, 'login')


