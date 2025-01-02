import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://the-internet.herokuapp.com/basic_auth'

driver=webdriver.Chrome()
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.maximize_window()
time.sleep(3)
# usingtitle
#u
# expedtedtitle="The Internet"
# if expedtedtitle==driver.title:
#     print('passed')
# else:
#     print('failed')

expedtedline="Congratulations! You must have the proper credentials."
actualline=driver.find_element(By.XPATH,'//*[@id="content"]/div/p').text

print(actualline)
if expedtedline==actualline:
    print('passed')
else:
    print('failed')
driver.quit()
