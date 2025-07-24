from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def take_samsung_store_screenshot():
    """
    Automate opening Samsung Store and taking a screenshot
    """
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Optional: Run in headless mode (remove this line to see the browser)
    # chrome_options.add_argument("--headless")
    
    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        print("Opening Samsung Store...")
        
        # Navigate to Samsung Store
        driver.get("https://www.samsung.com/us/")
        
        # Wait for the page to load completely
        time.sleep(5)
        
        # Maximize the window for better screenshot
        driver.maximize_window()
        
        # Additional wait to ensure all elements are loaded
        time.sleep(3)
        
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        # Take screenshot
        screenshot_path = "screenshots/samsung_store_homepage.png"
        driver.save_screenshot(screenshot_path)
        
        print(f"Screenshot saved successfully at: {screenshot_path}")
        
        # Optional: Get page title for verification
        page_title = driver.title
        print(f"Page title: {page_title}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")

def take_samsung_store_screenshot_advanced():
    """
    Advanced version with better error handling and customization
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Execute script to hide webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    try:
        print("Opening Samsung Store (Advanced)...")
        
        # Set implicit wait
        driver.implicitly_wait(10)
        
        # Navigate to Samsung Store
        driver.get("https://www.samsung.com/us/")
        
        # Wait for page to load
        driver.implicitly_wait(10)
        time.sleep(5)
        
        # Maximize window
        driver.maximize_window()
        time.sleep(2)
        
        # Create screenshots directory
        os.makedirs("screenshots", exist_ok=True)
        
        # Get timestamp for unique filename
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/samsung_store_{timestamp}.png"
        
        # Take full page screenshot
        driver.save_screenshot(screenshot_path)
        
        print(f"Screenshot saved: {screenshot_path}")
        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
    finally:
        driver.quit()
        print("Automation completed.")

if __name__ == "__main__":
    # Run the basic version
    take_samsung_store_screenshot()
    
    # Uncomment below to run the advanced version
    # take_samsung_store_screenshot_advanced()
