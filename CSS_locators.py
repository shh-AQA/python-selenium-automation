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
driver.get('https://www.amazon.com/')

## 'Search Amazon input field' and connect using CSS by ID using '#''
# this example would usually be By.ID, 'twotabsearchtextbox'
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

## 'Search Amazon input field' and connect using CSS by tag and ID'
# to be implicit, can include tag as well (input in this case)
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

## 'Search Amazon input field' and connect using CSS by class'
driver.find_element(By.CSS_SELECTOR, '.nav-input')

## 'Search Amazon input field' and connect using CSS by multiple classes'
# use multiple classes to narrow down search
# string together using a period in between each class, hoever, try to connect using as few as possible
# even trying to use different combinations of the available classes. order does not matter
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute')

## 'Search Amazon input field' and connect using CSS by class and tag'
driver.find_element(By.CSS_SELECTOR, 'span.nav-input')

## 'Search Amazon input field' and connect using CSS by tag, ID and class' COMBINING ALL OF THE ABOVE!!
# order does not matter but best practice is to put tag first
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-input')

## 'Search Amazon input field' and connect using CSS by attribute
# NOTE: can technically connect to ID's and classes using this syntax as they are also attributes
# but primarily used in edge case scenarios
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords']")
# can also be combined with other search options, ex. tag and class
driver.find_element(By.CSS_SELECTOR, "input.nav-input[name='field-keywords']")

## 'Search Amazon input field' and connect using CSS with contains'
driver.find_element(By.CSS_SELECTOR, "[name*='keywords']") #syntax is * before equal sign
# can also be used with class when you want to search for partial matches
# useful in cases where the there are multiple classes with what appears to be auto-generated data
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsBaseButton']")
# combined classes ex
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsBaseButton'][class*=''styles_ndsButtonPrimary]")
# combined with a tag
driver.find_element(By.CSS_SELECTOR, "button[class*='styles_ndsBaseButton'][class*=''styles_ndsButtonPrimary]")

 ## NOTES:
 # CSS_Selectors cannot connect t0 text.  In that case, use XPATH