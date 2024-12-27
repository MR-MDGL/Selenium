#locators address identify web element uniquely on the web page
# id      name      linktext    partial linktext        xpath
import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#
# from Silenium.basic import actual

# service_obj = Service(r'E:\driver SDET\chromedriver-win64\chromedriver.exe')
driver=webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
time.sleep(2)




#serching for t shirt
# driver.find_element(By.ID,'search_query_top').send_keys("T shirt")
# time.sleep(2)
# driver.find_element(By.NAME,'submit_search').click()
# time.sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT,'Faded Short Sleeve T-shirts').click()
# time.sleep(2)
# expected='Faded Short Sleeve T-shirts - My Shop'
# actuall=driver.title
# if expected==actuall:
#     print('true')
# else:
#     print('false')
# driver.find_element(By.CLASS_NAME,'logo img-responsive').click()





#find total num of slider
# slider=driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print('total num of homeslider is ',len(slider) )



# img=driver.find_elements(By.TAG_NAME,"img")
# print('total num of images on website  is ',len(img) )

# tags=driver.find_elements(By.TAG_NAME,"a")
# print('total num of homeslider is ',len(tags) )

# btn=driver.find_elements(By.TAG_NAME,"button")
# print('total num of btn  is ',len(btn) )

# =driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print('total num of homeslider is ',len(slider) )

abc=driver.find_elements(By.CLASS_NAME,'sf-menu')
for i in abc:
    print(i.text)


driver.close()
