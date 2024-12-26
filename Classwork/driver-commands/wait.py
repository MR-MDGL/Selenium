# import time
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
wait = WebDriverWait(driver, timeout=10,poll_frequency=2)       #poll frequency is second in which it cheacks for the element to be loaded or not
# # element = wait.until(EC.visibility_of_element_located((By.ID, "element_id")))
#




#  # on google ------implicit and explicit
# driver.get("https://www.google.com/")
# driver.implicitly_wait(5)
# # driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys('selenium python')
# # Explicit wait------------
# element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
# element.send_keys('hello')
# element.submit()
# time.sleep(3)
# driver.close()



# driver.get('https://opensource-demo.orangehrmlive.com/')
# user_name=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@name='username]"))).send_keys('Admin')
# pass_word=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@name='password']"))).send_keys('admin123')
# login_btn=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@type='submit']'))).click()
# time.sleep(3)
# driver.close()




# Implicit Waits: Global, waits for elements up to a set time.-----------------------
#             from selenium import webdriver
#             driver = webdriver.Chrome()
#             driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear