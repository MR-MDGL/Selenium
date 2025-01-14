import time
from typing import KeysView

from selenium import  webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://www.google.com/')
act=ActionChains(driver)
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys('my search querry ')


act.key_down(Keys.CONTROL)
act.send_keys('a')
act.send_keys('c')
act.send_keys(Keys.BACKSPACE)
time.sleep(1)
act.key_up(Keys.CONTROL)
act.perform()


act.key_down(Keys.CONTROL)
act.send_keys('a')
act.send_keys(Keys.BACKSPACE)
time.sleep(1)
act.key_up(Keys.CONTROL)
act.perform()


act.key_down(Keys.CONTROL)
act.send_keys('v')
act.send_keys(Keys.BACKSPACE)
time.sleep(1)
act.key_up(Keys.CONTROL)
act.perform()




time.sleep(3)
driver.quit()

