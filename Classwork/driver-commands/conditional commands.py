import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()




# driver.get("https://www.facebook.com/")
# driver.
# time.sleep(1)
# logo=driver.find_element(By.XPATH,"//*[@class='fb_logo _8ilh img']")
# time.sleep(1)
# input=driver.find_element(By.XPATH,"//*[@class='inputtext _55r1 _6luy']")           #will give true for search bar only
#
# input.click()
#
# print(f'displayed {logo.is_displayed()}')
# print(f'enabled {logo.is_enabled()}')
# print(f'input selected or not {input.is_selected()}')
# driver.close()



driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM").click()
driver.forward()
title=driver.title
print(title)

time.sleep(5)

driver.close()


