import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://evernote.com/pdf-editor?utm_source=bing_ads&t_s=microsoft_ads&t_cid=486148767&t_agid=1233653124066952&t_crid=kwd-77103674119852%3Aloc-90&t_crname=pdf+editor&t_match_type=e&t_network=o&t_device=c&t_validation=486148767&t_cname=Manual_US_Campaign_Registrations_PDFEdit&msclid=12e73c97659e11d285be5bedad4b4caf&t_agname=PDFEditor_Keywords&referrer=xina%3D5e485196-b526-43fb-9908-0d5a70aee83f")
driver.maximize_window()
time.sleep(5)


driver.find_element(By.XPATH,'//input[@type="file"]').send_keys("E:\BEBO-Tech\gitSelenium\Selenium\Classwork\file download and upload\leo_visions-K2HIvGR9CPQ-unsplash.jpg")      #location of the file which gonna upload

time.sleep(4)