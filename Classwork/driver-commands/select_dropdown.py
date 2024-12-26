from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.implicitly_wait(2)
country=Select(driver.find_element(By.ID,'country'))
# country.select_by_index(2)        #using select index method
#-------created obj and iterated through
# op=country.options
# for i in op:
#     print(i.text)
# time.sleep(5)


days=driver.find_elements(By.XPATH,"//*[@type='checkbox' and @class='form-check-input']")
for i in days:
    i.click()
time.sleep(2)
for i in days:

    i.click()


driver.quit()
































# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/automation-practice-form')
#
# fname = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys('fname')
# lname = driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys('lname')
# email = driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys('ege@abcl.com')
# phoneno = driver.find_element(By.XPATH, '//*[@id="userNumber"]').send_keys('23456789')
#
# state_dropdown = driver.find_element(By.XPATH, '//*[@id="state"]')
# select_state = Select(state_dropdown)
# select_state.select_by_visible_text('Uttar Pradesh')
#
# time.sleep(5)
# driver.quit()