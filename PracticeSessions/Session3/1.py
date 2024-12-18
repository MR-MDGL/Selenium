# 1. Chained Locators
# Open https://www.wikipedia.org.
# Locate the search box inside a diy using chained locators (e.g., find the Ly first and
# then locate the input element inside it).
# • Enter "Automation testing" into the search box.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.wikipedia.org.')
driver.find_element(By.XPATH,"/html/body/main/div[2]/form/fieldset/div/input" ).send_keys('Automation testing')
time.sleep(2)

# driver.find_element("//*[@class='pure-button pure-button-primary-progressive']").click()
time.sleep(5)
driver.close()
