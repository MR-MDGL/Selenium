from selenium import webdriver

# driver = webdriver.Chrome()           use only wen we want to opent he browser

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver

def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Edge(options=ops)
    return driver



driver = headless_chrome()
driver.get("https://www.google.com")
print(driver.title,"from chrome")
driver.quit()


driver = headless_edge()
driver.get('https://www.google.com')
print(driver.title,'from edge')
driver.quit()
        



















'''
headless mode----- will not open the browser and only give ouput (genrally we dont need to open the browser 
we just want the output so we use this )

head mode is the basic mode opens browswr



'''