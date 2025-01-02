import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get('http://www.deadlinkcity.com/')
time.sleep(1)
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
failed_link=0
succes_link=0

for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        failed_link+=1
        print('broken link',res)
    else:
        succes_link+=1
        print('valid link',res)

print(f'total links {len(links)}')
print(f'total dead links{failed_link}')
print(f'total working links {succes_link}')
time.sleep(2)
driver.close()