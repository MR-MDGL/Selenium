# 1. Write a login script for the New Tours website at
# ht s://demo. uru99.com/test/newtours
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.guru99.com/test/newtours')
time.sleep(2)
user_name=driver.find_element(By.NAME,'userName').send_keys('Admin')
time.sleep(2)
login_pass=driver.find_element(By.NAME,'password').send_keys('admin')
time.sleep(2)
submit_btn=driver.find_element(By.NAME,'submit').click()
time.sleep(3)
driver.close()



