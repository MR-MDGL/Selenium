import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://www.orangehrm.com/')
driver.save_screenshot(os.getcwd()+"homepage.png")
# driver.save_screenshot(r"C: full path")




time.sleep(3)
driver.quit()




'''


driver.save_screenshot(pathof your pc)
driver.save_screenshot(os.getwed()+"//homepage.png"             #dynamic path 


'''