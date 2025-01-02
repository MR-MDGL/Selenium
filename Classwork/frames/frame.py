import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

driver.get('https://www.hyrtutorials.com/p/frames-practice.html')
driver.switch_to.frame(1)
dropdown_element = driver.find_element(By.XPATH, '//*[@id="selectnav1"]')
dropdown_element.click()
select = Select(dropdown_element)
select.select_by_index(2)
print('secected executed ')
time.sleep(5)
driver.close()
