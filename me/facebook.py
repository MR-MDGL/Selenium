'''
visit email in fb login page then find all elements preceding and following and print its count and tag name
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
time.sleep(2)
preceding_element = driver.find_elements(By.XPATH,"//input[@name='email']/preceding::*")
count = 0
for i in preceding_element:
    count += 1
    print(f"Preceding Tag Names are: {i.tag_name} and Count is: {count}")
print(f"Total Elements are: {count}\n")
# print(len(preceding_element))
time.sleep(2)
user_name = driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abcd@gmail.com")
following_element = driver.find_elements(By.XPATH,"//input[@name='email']/following::*")
count = 0
for i in following_element:
    count+=1
    print(f"Following Tag Names are: {i.tag_name} and its Respective Count is: {count}")
print(f"Total Elements are: {count}")
print(len(following_element))
time.sleep(2)
driver.close()
