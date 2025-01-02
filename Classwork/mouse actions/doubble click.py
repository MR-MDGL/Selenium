import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()

driver.maximize_window()
url="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3"
driver.get(url)
act=ActionChains(driver)
framee=driver.find_element(By.XPATH,'//*[@id="iframeResult"]')
driver.switch_to.frame(framee)
inputfeild=driver.find_element(By.XPATH, '//*[@id="field1"]')
inputfeild.clear()
inputfeild.send_keys('sunil')



dbclkbtn=driver.find_element(By.XPATH,'/html/body/button')
act.double_click(dbclkbtn).perform()



expectedd='sunil'
actuall=driver.find_element(By.XPATH,'//*[@id="field2"]').text
if expectedd==actuall:
    print(' Matched')
else:
    print('Failed')






time.sleep(2)
driver.quit()







