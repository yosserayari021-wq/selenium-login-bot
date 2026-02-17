from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # Used to locate elements
from selenium.webdriver.common.keys import Keys # Used for keyboard actions
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Setup the Browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 2. Navigate to the login page
    print("Opening browser...")
    driver.get("http://quotes.toscrape.com/login")
    
    # 3. Locate the elements
    # We find the boxes by their ID attribute
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    # 4. Perform Actions
    print("Typing credentials...")
    username_field.send_keys("MyComputerEngineerName") # Type anything
    password_field.send_keys("Password123")
    
    # 5. Submit the form
    # We can either find the 'Login' button and click it, 
    # or just press 'ENTER' on the keyboard.
    password_field.send_keys(Keys.ENTER)
    
    print("Login successful! Waiting to see the result...")
    
    # Wait 5 seconds so you can see the 'Logout' link appear 
    # (proving you are logged in)
    time.sleep(5)

finally:
    # Always close the browser, even if there's an error
    print("Closing browser.")
    driver.quit()