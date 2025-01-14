import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()

driver.maximize_window()
url='https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette'
driver.get(url)
act=ActionChains(driver)

slider=driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
# destination=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
act.click_and_hold(slider).move_by_offset(50, 0).release().perform()

# print(source)

time.sleep(2)
driver.quit()

