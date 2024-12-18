# 1. Locate Element by ID
# Open a website of your choice (e.g., https://www.wikipedia.org).
# • Locate the search box by ID and enter the text "Selenium Python."
# Click the search button.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.wikipedia.org')
serch=driver.find_element(By.NAME,'search').send_keys('Selenium Python.')
time.sleep(5)
serch_btn=driver.find_element(By.CLASS_NAME,'pure-button').click()

time.sleep(5)
driver.close()
