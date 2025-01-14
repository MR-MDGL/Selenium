import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://demo.guru99.com/test/simple_context_menu.html')
act=ActionChains(driver)

dbclickbtn=driver.find_element(By.XPATH, '//*[@ondblclick="myFunction()"]')
act.double_click(dbclickbtn).perform()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(2)

driver.quit()