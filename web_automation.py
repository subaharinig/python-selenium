from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create Chrome options (optional)
options = Options()
options.add_argument("--window-size=1920x1080")

# Create WebDriver instance
driver = webdriver.Chrome(options=options)

time.sleep(2)

# Navigate to a website
driver.get("https://www.linkedin.com/in/suba-harini-1b07a1296/")

# Get page title
print(driver.title)
time.sleep(5)

# Close the browser
driver.quit()