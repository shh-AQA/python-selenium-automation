from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')



# 2. Click SignIn button
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(5)

# 3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# 4. Verify SignIn page opened:
# actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
# expected_result = "Sign into your Target account"
#
# assert expected_result in actual_result, f'Expected: {expected_result}, Actual: {actual_result}'
# print('Test Case Passed')


# “Sign into your Target account” text is shown,

# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.ID, "login")

