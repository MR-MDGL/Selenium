import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Contact').click()
time.sleep(2)
driver.find_element(By.ID,'email').send_keys('abc@gmail.com')
time.sleep(2)
driver.find_element(By.ID,'id_order').send_keys('12345')
time.sleep(2)
driver.find_element(By.NAME,'message').send_keys('a temporary message xyz abc')
list1=driver.find_elements(By.TAG_NAME,'option')
list1[2].click()
time.sleep(2)
driver.find_element(By.ID,'submitMessage').click()
time.sleep(5)
driver.close()
