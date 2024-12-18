# 4. Locate Element by Tag Name
# • Open https://demoqa.com/automation-practice-form.
# • Locate all input fields by their tag name and print their placeholder
# attribute.


from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)
inputss=driver.find_elements(By.TAG_NAME,'input')
print(len(inputss))


time.sleep(3)
driver.close()