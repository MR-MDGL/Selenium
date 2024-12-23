# l. Write a script to maximize the browser window and then print its current size.



import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.python.org/")
driver.maximize_window()
# print(driver.get_window_size())
# print('-----------------------')
# # 2. How would you retrieve the title of a webpage using Selenium in Python? Write the code
# # snippet.
# print(driver.title)
# print('-----------------------')

# curr=driver.current_url
# # 3. Write a script to fetch the current URL ofa webpage and verify if it matches the expected
# expcted='https://www.python.org/'
# print('-----------------------')
# # 4. Using Selenium, how can you retrieve the source code of the loaded page? Provide the code
# # snippet.
# if curr==expcted:
#     print(True,'matched')
# else:
#     print(False,'not matched ')
#
# print(driver.page_source)


# 5. Write a script to check whether a specific webpage is loaded by verifying the presence of a
# keyword in the title.
word='Python'
if word in driver.title:
    print(True)
else:
    print(False)



driver.quit()