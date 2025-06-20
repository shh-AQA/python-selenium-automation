from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# locators:
# By.ID, preferred way to locate elements
driver.find_element(By.ID, 'twotabsearchtextbox')

#By.XPATH
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

#By.XPATH, any tag
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']") #replaced 'input' tag with *, which is a wildcard

#By.XPATH, using a combination of attributes
#Amazon logo
driver.find_element(By.XPATH, "//a[@aria-label='Amazon' and @lang='en']") #using 'and'
driver.find_element(By.XPATH, "//*[@aria-label='Amazon' and @lang='en']") #combination of attributes and wild card
driver.find_element(By.XPATH, "//*[@lang='en' and @aria-label='Amazon']") #order of attribute in DOM doesn't matter

#By.XPATH USING TEXT
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']") #combined text and attribute

#By.XPATH, using 'contains'
driver.find_element((By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")) #finds a partial match of attribute

#By.XPATH, parent --> child nodes
driver.find_element((By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']"))