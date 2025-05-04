from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = "laptop"
fileno = 0
wait = WebDriverWait(driver, 10)

for i in range(1, 4):
    driver.get(f"http://www.amazon.in/s?k={query}&page={i}&crid=234WC15ZUST3N&sprefix=lap%2Caps%2C432&ref=nb_sb_noss_2")

    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "puis-card-container")))
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        print(f"Total items on page {i}: {len(elems)}")
        
        for elem in elems:
            d = elem.get_attribute("outerHTML")
            with open(f"data/{query}_{fileno}.html", "w", encoding='utf-8') as f:
                f.write(d)
            fileno += 1
    except:
        print(f"Could not find product cards on page {i}")

    time.sleep(5)

driver.close()
