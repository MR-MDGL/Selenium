# 3. Locate Element by Spath
# Open https://demo.guru99.com/test/pgvy!ours/.
# Locate the "REGISTER" link using th and click on it.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.guru99.com/test/newtours/')
driver.find_element(By.XPATH,"//*[@name='submit']" ).click()

time.sleep(2)
driver.close()