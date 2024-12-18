# 2. Locate Element with Attributes and Text
# Open https://demo.guru99.wn/tes nyy40urs/.
# Locate the "Submit" button on the login form using an that matches both
# attributes and text.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.guru99.com/test/newtours/')
driver.find_element(By.XPATH,"//*[@name='submit']" ).click()

time.sleep(2)
driver.close()
