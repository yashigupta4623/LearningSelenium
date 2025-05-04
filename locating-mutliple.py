from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query = "laptop"

for i in range(1, 4):
    driver.get("https://www.amazon.com")
    elem = driver.find_element(By.CLASS_NAME, "laptop")
    print(f"Iteration {i}:")
    for elem in elem:
        print(elem.text)    

time.sleep(5) 
driver.close()