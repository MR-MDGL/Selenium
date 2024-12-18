# 2.
# Locate Element by Name
# • Go to https://www.google.com.
# • Locate the search box by the name attribute.
# • Perform a search for "Python programming language."
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com.")
time.sleep(2)
driver.find_element(By.NAME,'q').send_keys('Python programming language')
time.sleep(2)
driver.find_element(By.NAME,'btnK').click()

time.sleep(3)
driver.close()


