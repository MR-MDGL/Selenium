import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()

driver.maximize_window()
url="https://demo.nopcommerce.com/register?returnUrl=%2F"
driver.get(url)
act=ActionChains(driver)


computer=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/a')
notebook=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[2]/a')


act.move_to_element(computer).move_to_element(notebook).click().perform()
# computer=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[2]/li[1]/a').click()


expected_title='nopCommerce demo store. Notebooks'
actual_title=driver.title
if expected_title==actual_title:
    print('Title Matched')
else:
    print('Failed')

time.sleep(2)
driver.quit()



























'''
methods
build ()        create steps sequence
perform()       execute the steps


'''