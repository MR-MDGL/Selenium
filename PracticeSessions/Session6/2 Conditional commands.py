from selenium.webdriver.common.by import By

url='https://www.w3schools.com/html/html_forms.asp'
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get(url)
#
# # l. Write a script to verify whether a button element is enabled before clicking on it.
btn=driver.find_element(By.XPATH,"//button[@class='ws-btn']" )
print(btn.is_enabled())
btn.click()


# 2. How can you check if a checkbox is selected? Write a Selenium script to verify the state ofa
# checkbox.
# time.sleep(2)
box=driver.find_element(By.ID,"vehicle1")
print(box.is_selected())
driver.quit()
