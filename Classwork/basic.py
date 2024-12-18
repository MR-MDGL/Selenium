#open browser
#pass url https://www.google.com/
#capture text box
#send values "silenium"
#validation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time




#----------------approch 1
service_obj = Service(r'E:\driver SDET\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/")
textbox = driver.find_element(By.NAME, 'q')
textbox.send_keys("Selenium")
time.sleep(2)
search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()
time.sleep(2)


#validation
expected='Selenium - Google Search'
actual=driver.title
if expected ==actual:
    print('passed')
else:
    print('failed')



#-------------approch 2
# approch 1
# service_obj = Service(r'E:\driver SDET\chromedriver-win64\chromedriver.exe')

#
# driver = webdriver.Chrome()
#
#
# driver.get("https://www.google.com/")
# textbox = driver.find_element(By.NAME, 'q')
# textbox.send_keys("Selenium")
# time.sleep(3)
