import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()

driver.maximize_window()
url="https://swisnl.github.io/jQuery-contextMenu/demo.html"
driver.get(url)
act=ActionChains(driver)

DbClkkBtn=driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/p/span')
copybtn=driver.find_element(By.XPATH,'/html/body/ul/li[3]/span')
act.context_click(rightClkkBtn).perform()
act.move_to_element(copybtn).click().perform()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text)

expected_text='clicked: copy'
actual_text=alert.text
if expected_text==actual_text:
    print('Passed')
else:
    print('Failed')
alert.accept()








time.sleep(2)
driver.quit()







