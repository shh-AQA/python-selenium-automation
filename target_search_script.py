from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

# init driver
# 3 A's: Arrange
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

#input text in search field and click on search icon
# 3 A's: Act
driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(3)

#verification
# 3 A's: Assertions
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
assert expected_text in actual_text, f"Error. Expected Text: {expected_text} not in Actual Text: {actual_text}"

print("Test Case Passed")

driver.quit()