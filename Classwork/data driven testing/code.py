from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open Flipkart
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load completely

    # Handle login popup if it appears
    try:
        close_login_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_login_popup.click()
        time.sleep(1)
    except:
        print("Login popup did not appear.")

    # Locate the Electronics tab
    electronics_tab = driver.find_element(By.XPATH, "//div[text()='Electronics']")

    # Hover over the Electronics tab
    actions = ActionChains(driver)
    actions.move_to_element(electronics_tab).perform()
    time.sleep(2)  # Wait for dropdown to load

    # Hover over the "All" section
    all_section = driver.find_element(By.XPATH, "//a[contains(text(),'All')]")
    actions.move_to_element(all_section).perform()
    time.sleep(2)  # Wait for submenu to load

    # Click on "Bluetooth Speaker"
    bluetooth_speaker = driver.find_element(By.XPATH, "//a[contains(text(),'Bluetooth Speakers')]")
    bluetooth_speaker.click()

    # Allow time to view the next page
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
