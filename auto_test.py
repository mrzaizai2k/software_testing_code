from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import *

# Path to your ChromeDriver executable
def initialize_driver(driver_path, chrome_options):
    webdriver_service = Service(driver_path)
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    return driver, webdriver_service

config = read_config(path = "config.yml")

driver_path = config['driver_path']
# driver_path = "chromedriver-mac-x64/chromedriver-mac-x64/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")

driver, webdriver_service = initialize_driver(driver_path, chrome_options)


# Open the URL in the Chrome browser
driver.get("https://www.calculator.net/bmi-calculator.html")

# Check if the login page is opened by searching for the username input field
# username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
time.sleep(1)

def input_values(driver, config):
    metric_link = driver.find_element(By.XPATH, '//a[contains(text(), "Metric Units")]')
    metric_link.click()


    age_input = driver.find_element(By.ID, 'cage')
    age_input.clear()
    age_input.send_keys(config['age'])

    height_input = driver.find_element(By.ID, 'cheightmeter')
    height_input.clear()
    height_input.send_keys(config['height'])

    weight_input = driver.find_element(By.ID, 'ckg')
    weight_input.clear()
    weight_input.send_keys(config['weight'])
    
    # Select gender based on config
    time.sleep(2)
        # Select gender based on config
    if config['gender'] == 'male':
        radio = driver.find_element(By.XPATH,"//label[contains(text(),'Male')]")
        radio.click()
    elif config['gender'] == 'female':
        radio = driver.find_element(By.XPATH,"//label[contains(text(),'Female')]")
        radio.click()
    else:
        print("Invalid gender specified in config")


    # Click on the "Calculate" button
    calculate_button = driver.find_element(By.XPATH, '//input[@value="Calculate"]')
    calculate_button.click()

for i in range(4):
    try:
        print(f'Test for case{i+1}')
        input_values(driver, config[f'case{i+1}'])
        time.sleep(2)
    except Exception as e:
        print(f"error: {e}")
    


time.sleep(10)
# Close the browser window
# driver.quit()
