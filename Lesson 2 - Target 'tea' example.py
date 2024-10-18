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


# search field => enter 'tea'
driver.find_element(By.ID, 'search').send_keys('tea')

# search button => 'click'
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(4)

# verification
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
expected_result = 'tea'

assert expected_result in actual_result, f'Expected: {expected_result}, Actual: {actual_result}'
print('Test Case Passed')

driver.quit()