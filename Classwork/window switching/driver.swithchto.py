import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
p=driver.current_window_handle
click=driver.find_element(By.XPATH,'/html/body/footer/section/div[2]/div/div/div[1]/div/ul/li[1]/a').click()

# driverCurrentWindow=driver.current_window_handle
# print(driverCurrentWindow)

var=driver.window_handles
print(type(var),var)


expectedTitle='Get to Know Us |  Innovating HR Solutions | OrangeHRM'


for i in var :
    time.sleep(2)
    if i != p:
        driver.switch_to.window(i)
        actualTitle=driver.title
        if expectedTitle==actualTitle:
            print('True both matched')
        else:
            print('failed')





time.sleep(3)
driver.quit()




'''
# driver.swithchto




driver.current_window_handle
driver.window_handles


driver.save_screenshot(pathof your pc)
driver.save_screenshot(os.getwed()+"//homepage.png"             #dynamic path 


'''