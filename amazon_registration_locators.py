from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')
driver.find_element(By.XPATH, "//a[@class='nav-a']").click()


# Find the most optimal locators for Create Account on amazon.com (Registration) page elements
#
#
sleep(4)
# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")


# 'Create Account'
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

# 'Your name' field
driver.find_element(By.ID, 'ap_customer_name')

# 'Mobile number or mail' field
driver.find_element(By.ID, 'ap_email')

# 'Password' field
driver.find_element(By.ID, 'ap_password')

# Password requirement
driver.find_element(By.XPATH, "//div[@class='a-alert-content' and text()='Passwords must be at least 6 characters.']")

# 'Re-enter' password field
driver.find_element(By.ID, 'ap_password_check')

# 'Continue or Create Account' button
driver.find_element(By.ID, 'continue')

# 'Conditions of Use' link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# 'Privacy Notice' link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# 'Sign-in link'
driver.find_element(By.XPATH, "//a[class='a-link-emphasis']")


