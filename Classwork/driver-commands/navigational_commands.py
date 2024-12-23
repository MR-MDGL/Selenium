import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.minimize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@title='Sign up for Facebook']").click()
time.sleep(3)
print(driver.title)
driver.back()
print(driver.current_url)
time.sleep(3)
driver.forward()
print(driver.title)

driver.quit()
