
#-----------------working----------------


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# location = os.getcwd()
#
# # for chrome
# def chrome_setup():
#     preferences = {"download.default_directory":location}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs",preferences)
#     driver = webdriver.Chrome(options=ops)
#     return driver
#
#
# driver = chrome_setup()
# driver.get("https://unsplash.com/photos/a-foggy-view-of-the-golden-gate-bridge-K2HIvGR9CPQ")
# driver.maximize_window()
# btn=driver.find_element(By.XPATH,"//a[normalize-space()='Download free']")
# btn.click()
# # time.sleep(15)
# # driver.implicitly_wait()
# driver.quit()
#








#---------with explicit wait for file to be downloaded
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

location = os.getcwd()

# for chrome
def chrome_setup():
    preferences = {"download.default_directory": location, "download.prompt_for_download": False}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

def wait_for_downloads(download_dir, timeout=60):
    seconds = 0
    while seconds < timeout:
        if any(filename.endswith('.jpg') for filename in os.listdir(download_dir)):  # Adjust the extension as needed
            return True
        time.sleep(1)
        seconds += 1
    return False

driver = chrome_setup()
driver.get("https://unsplash.com/photos/a-foggy-view-of-the-golden-gate-bridge-K2HIvGR9CPQ")
driver.maximize_window()

# Adding explicit wait for the button to be clickable
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Download free']")))
btn.click()

# Wait for the file to be downloaded
if wait_for_downloads(location):
    print("File downloaded successfully.")
else:
    print("File download timed out.")

driver.quit()

