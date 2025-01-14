import time
from selenium import webdriver
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.orangehrm.com/')
time.sleep(2)



#scroll down by moving pixels
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print('pixles moved',value)





#scroll till element is visible
# image=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/section[2]/div[4]/div/div[1]/div[1]/div/img')
# driver.execute_script("arguments[0].scrollIntoView();", image)
# value=driver.execute_script("return window.pageYOffset;")
# print('pixles moved',value)





#scroll down till page ends
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
time.sleep(2)
value=driver.execute_script("return window.pageYOffset;")
print(' moved',value)








time.sleep(3)
driver.quit()








'''
javascript executor 


'''