# #relative xpath
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get('https://online.btes.co.in/login/index.php')
# driver.find_element(By.XPATH,'//*[@name="username"]').send_keys('sunil@123')
# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('$uniL121*#')
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='loginbtn']").click()
# time.sleep(2)
# driver.close()



#absolutie xpath
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://online.btes.co.in/login/index.php')
driver.find_element(By.XPATH,'//*[@name="username"]').send_keys('sunil@123')
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('$uniL121*#')
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='loginbtn']").click()
time.sleep(3)
expected='Sunil Mudgil'
actualName=driver.find_element(By.XPATH,"//*[@class='usertext mr-1']").text
if expected==actualName:
    print(True)
else:
    print(False)
driver.find_element(By.XPATH,"//*[@class='card-img dashboard-card-img']").click()
time.sleep(3)
actualName2=driver.find_element(By.XPATH,"//*[@class='page-header-headings']/h1").text
expected2="SDET with Python-AI for IT&R"
time.sleep(5)
if expected2==actualName2:
    print(True,'name is ok')
else:
    print(False,'name is wrongggggg............')
# print(expected2,'------',actualName2)

time.sleep(5)
driver.close()

# comment