from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Go to LinkedIn profile page (replace with the actual profile URL)
profile_url = 'https://www.linkedin.com/in/example/'
driver.get(profile_url)

# Wait for the page to load
time.sleep(5)

# Example: Extract specific sections (e.g., About, Experience, Education)
try:
    about_section = driver.find_element(By.XPATH, "//section[contains(@class, 'about')]").text
    experience_section = driver.find_element(By.XPATH, "//section[contains(@class, 'experience')]").text
    education_section = driver.find_element(By.XPATH, "//section[contains(@class, 'education')]").text
    
    print("About Section:", about_section)
    print("Experience Section:", experience_section)
    print("Education Section:", education_section)
except Exception as e:
    print("Error extracting data:", e)

# Close the browser
driver.quit()
