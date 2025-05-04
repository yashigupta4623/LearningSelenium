from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options to use your logged-in profile
options = Options()
options.add_argument("user-data-dir=C:/Users/ASUS/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Default")  # or "Profile 1", etc.

# Launch Chrome with profile
driver = webdriver.Chrome(options=options)

# Proceed with automation
driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
time.sleep(50)
driver.close()
