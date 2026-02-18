from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    print("Opening browser...")
    driver.get("http://quotes.toscrape.com/login")
    
  
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    print("Typing credentials...")
    username_field.send_keys("MyComputerEngineerName") 
    password_field.send_keys("Password123")
   
    password_field.send_keys(Keys.ENTER)
    
    print("Login successful! Waiting to see the result...")
    
    time.sleep(5)

finally:
    print("Closing browser.")
    driver.quit()
