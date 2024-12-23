import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)
title=driver.title
url=driver.current_url
sourceCode=driver.page_source
print(title)
print(url)
print(sourceCode)

driver.close()
