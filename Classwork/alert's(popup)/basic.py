import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
time.sleep(2)
alertclick=driver.switch_to.alert
time.sleep(2)
alertclick.accept()


confirmclk=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
time.sleep(2)
confirm=driver.switch_to.alert
confirm.accept()


confirmclk=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
time.sleep(2)
confirm=driver.switch_to.alert
confirm.dismiss()
time.sleep(3)


promptbtn=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(2)
promptclk=driver.switch_to.alert
promptclk.send_keys('hellow')
promptclk.accept()



time.sleep(3)
driver.quit()