import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
time.sleep(1)
driver.find_element(By.ID,'email_create').send_keys('xyy@gmail.com')
time.sleep(1)
driver.find_element(By.CLASS_NAME,'icon-user').click()
time.sleep(3)
driver.find_element(By.ID,'id_gender1').click()
time.sleep(1)
driver.find_element(By.ID,'customer_firstname').send_keys('testing')
time.sleep(1)
driver.find_element(By.ID,'customer_lastname').send_keys('website')
time.sleep(1)
driver.find_element(By.ID,'passwd').send_keys('12345')
time.sleep(1)
driver.find_element(By.ID,'days').send_keys('5')
time.sleep(1)
lst=driver.find_elements(By.CLASS_NAME,'months')
lst[3].click()

time.sleep(5)
driver.close()