import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://www.globalsqa.com/demo-site/draganddrop/')

act = ActionChains(driver)
iframe = driver.find_element(By.XPATH, "//*[@id='post-2669']/div[2]/div/div/div[1]/p/iframe")
driver.switch_to.frame(iframe)

items = driver.find_elements(By.TAG_NAME, 'img')
destination = driver.find_element(By.XPATH, '//*[@id="trash"]')

for i in items:
    initial_item_location = i.get_attribute('outerHTML')
    act.drag_and_drop(i, destination).perform()
    time.sleep(1)

    # Re-locate items and the trash after the drag-and-drop operation
    items = driver.find_elements(By.TAG_NAME, 'img')  # Re-locate items
    trash_contents = driver.find_element(By.XPATH, '//*[@id="trash"]').get_attribute('innerHTML')

    assert initial_item_location not in trash_contents, f"Assertion failed! Item {i.get_attribute('src')} is still in the original location."
    print(f"Moved item: {i.get_attribute('src')} successfully.")
    assert
driver.switch_to.default_content()
driver.quit()