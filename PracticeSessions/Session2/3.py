# 3. Locate Element by Class Name
# • Open https://www.selenium.dev.
# • Locate the "Projects" link using its class name.
# • Click on the link.
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev.")
time.sleep(2)
list1=driver.find_elements(By.CLASS_NAME,'nav-item')
list1[3].click()



time.sleep(3)
driver.close()