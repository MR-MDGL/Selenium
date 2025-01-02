from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    wait = WebDriverWait(driver, 10)

    first_name_input = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="name"]') ))
    first_name_input.send_keys("John")

    last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastname")))
    last_name_input.send_keys("Doe")

    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("john.doe@example.com")

    male_radio = wait.until(EC.presence_of_element_located((By.ID, "sex-0")))
    male_radio.click()

    cricket_checkbox = wait.until(EC.presence_of_element_located((By.ID, "checkbox-0")))
    cricket_checkbox.click()

    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "continents")))
    country_dropdown.click()
    country_dropdown.find_element(By.XPATH, "//option[text()='Asia']").click()

    submit_button = wait.until(EC.presence_of_element_located((By.NAME, "submit")))
    submit_button.click()

finally:
    driver.implicitly_wait(5)
    driver.quit()