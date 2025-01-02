import time

from selenium import webdriver


ops=webdriver.ChromeOptions()
#
ops.add_argument('--disable-notification')

driver=webdriver.Chrome()
driver.get("https://whatmylocation.com/")
time.sleep(7)
driver.quit()