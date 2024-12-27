# #https://automationbookstore.dev/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://automationbookstore.dev/')
# email_locator = driver.find_element( locate_with(By.TAG_NAME, "li").below({By.ID,"pid2"})).text
# print(email_locator)
#near
# nearby_locator = driver.find_element(locate_with(By.TAG_NAME, "li").near({By.ID: "pid2"})).text
# print(nearby_locator)



#
# # below
# below_locator = driver.find_element(locate_with(By.TAG_NAME, "li").below({By.ID: "pid2"})).text
# print(below_locator)
#
# #near
# nearby_locator = driver.find_element(locate_with(By.TAG_NAME, "li").near({By.ID: "pid2"})).text
# print(nearby_locator)