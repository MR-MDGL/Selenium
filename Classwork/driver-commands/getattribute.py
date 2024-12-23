import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.opencart.com/")

time.sleep(2)
valuessss=driver.find_element(By.XPATH, "//*[@name='search']")
valuessss.send_keys('t-shirt')
print(valuessss.text)
print(valuessss.get_attribute('placeholder'))
print(valuessss.get_attribute('value'))



driver.quit()