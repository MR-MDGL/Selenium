import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()

driver.maximize_window()
url="http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver.get(url)
act=ActionChains(driver)

source=driver.find_element(By.XPATH,'//*[@id="box6"]')
destination=driver.find_element(By.XPATH,'//*[@id="box106"]')
act.drag_and_drop(source, destination).perform();
time.sleep(3)
washington=driver.find_element(By.XPATH,'//*[@id="box3"]')
unitedstates=driver.find_element(By.XPATH,'//*[@id="box103"]')
act.drag_and_drop(washington,unitedstates)



time.sleep(2)
driver.quit()
