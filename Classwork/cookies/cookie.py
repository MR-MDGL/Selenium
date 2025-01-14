# driver.getcookee
import time
from selenium import webdriver




# driver = webdriver.Chrome()        #   use only when we want to open the browser

# def headless_chrome():
#     ops = webdriver.ChromeOptions()
#     ops.add_argument("--headless")
#     driver = webdriver.Chrome(options=ops)
#     return driver




# driver = headless_chrome()

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

print(driver.title, "from chrome")

cookies = driver.get_cookies()
print(cookies, len(cookies))

driver.add_cookie({'name': 'hellow', 'value': '123'})

cookies = driver.get_cookies()
print(cookies, len(cookies))



# find a tool used in qe
# on which we will work on
# and show ppt