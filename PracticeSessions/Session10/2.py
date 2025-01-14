import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://practice.expandtesting.com/context-menu')
act=ActionChains(driver)

rightclkbtn=driver.find_element(By.XPATH,"//*[@id='hot-spot']")
act.context_click(rightclkbtn).perform()

driver.switch_to.alert.accept()
time.sleep(3)
# Close the driver
driver.quit()