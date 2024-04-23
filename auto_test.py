from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from utils import *

# Path to your ChromeDriver executable
def initialize_driver(driver_path, browser_options):
    webdriver_service = Service(driver_path)
    try:
        driver = webdriver.Chrome(service=webdriver_service, options=browser_options)
    except:
        driver = webdriver.Edge(service=webdriver_service)
    return driver, webdriver_service

config = read_config(path = "config.yml")

driver_path = config['driver_path']
# driver_path = "chromedriver-mac-x64/chromedriver-mac-x64/chromedriver"

browser_options = Options()
browser_options.add_argument("--no-sandbox")
browser_options.add_argument("--start-maximized")

driver, webdriver_service = initialize_driver(driver_path, browser_options)


# Open the URL in the Chrome browser
driver.get("https://www.calculator.net/bmi-calculator.html")

# Check if the login page is opened by searching for the username input field
# username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
time.sleep(1)

def check_result_BMI(driver, config):
    bmi_value = None
    status = None
    try:
        # Adjust the timeout as needed; here it's set to 10 seconds
        result_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.bigtext"))
        )
        result_text = result_element.get_attribute('innerHTML')

        # Step 2: Extract BMI and status from the result text
        bmi_value = re.search(r"BMI = (\d+\.?\d*)", result_text).group(1)
        status = re.search(r"<b>([^<]*)</b></font>", result_text).group(1)

        print ('bmi_value', bmi_value)
        print ('status', status)
        if bmi_value == str(config['bmi_value']) and status == config['status']:
            print ('Test case: Passed')
        else:
            print ('Test case: Not Passed')

    except Exception as e:
        print("Not appear result element:")

    # Step 3: Return the extracted data
    return bmi_value, status

def check_age_error(driver, config):
    # Validate age
    age = config['age']  # Default to 0 if 'age' key is missing
    
    # Input an invalid age
    age_input = driver.find_element(By.ID, 'cage')
    age_input.clear()
    age_input.send_keys(str(age))
    # Check for error message
    time.sleep(1)  # Wait for the error message to potentially load
    try:
        error_message = driver.find_element(By.XPATH, "//div[font[@color='red']]")
        if "Please provide an age between 2 and 120." in error_message.text:
            return True
        else:
            return False
    except:
        return False

def check_height_error(driver, config, error = "Please provide positive height value."):
    # Check for error message
    time.sleep(1)
    try:
        error_messages = driver.find_elements(By.XPATH, "//font[@color='red']")
        for message in error_messages:
            if error == message.text:
                return True
        return False
    except:
        return False


# def check_weight_error(driver, config, error = "Please provide positive height value."):

#     # Check for error message
#     time.sleep(1)
#     try:
#         error_message = driver.find_element(By.XPATH, "//font[@color='red']")
#         if error in error_message.text:
#             return True
#         else:
#             return False
#     except:
#         return False

def check_weight_error(driver, config, error="Please provide positive height value."):
    # Wait for a short period to ensure all elements are loaded
    time.sleep(1)
    
    try:
        # Find all error message elements
        error_messages = driver.find_elements(By.XPATH, "//font[@color='red']")
        for message in error_messages:
            if error == message.text:
                return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def check_neck_error(driver, config, error = "Neck need to be numeric."):

    # Check for error message
    time.sleep(1)
    try:
        error_messages = driver.find_elements(By.XPATH, "//font[@color='red']")
        for message in error_messages:
            if error == message.text:
                return True
        return False
    except:
        return False

def check_waist_error(driver, config, error = "Waist need to be numeric."):

    # Check for error message
    time.sleep(1)
    try:
        error_messages = driver.find_elements(By.XPATH, "//font[@color='red']")
        for message in error_messages:
            if error == message.text:
                return True
        return False
    except:
        return False


def input_values_BMI(driver, config):
    metric_link = driver.find_element(By.XPATH, '//a[contains(text(), "Metric Units")]')
    metric_link.click()

    age_input = driver.find_element(By.ID, 'cage')
    age_input.clear()
    if config['age'] is not None:
        age_input.send_keys(config['age'])

    height_input = driver.find_element(By.ID, 'cheightmeter')
    height_input.clear()
    if config['height'] is not None:
        height_input.send_keys(config['height'])


    weight_input = driver.find_element(By.ID, 'ckg')
    weight_input.clear() 
    if config['weight'] is not None:
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

    if config['age'] < 2 or config['age'] > 120:
        age_flag = check_age_error(driver, config)
        print("age_flag", age_flag)

    if config['height'] <= 0:
        height_flag = check_height_error(driver, config)
        print("height_flag", height_flag)

    if config['weight'] <= 0:
        weight_flag = check_weight_error(driver, config)
        print("weight_flag", weight_flag)


    check_result_BMI(driver, config)


for test_case in config['BMI_test']:
    try:
        print(f'\nTest for case: {test_case}')
        input_values_BMI(driver, config['BMI_test'][test_case])
        time.sleep(2)
    except Exception as e:
        print(f"error: {e}")
    
def check_result_body_fat(driver, config):
    body_fat_value = None
    status = None
    try:
        # Adjust the timeout as needed; here it's set to 10 seconds
        result_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.verybigtext font, font"))
        )
        result_text = result_element.get_attribute('innerHTML')

        # Step 2: Extract BMI and status from the result text
        body_fat_value = float(re.search(r"Body Fat: (\d+\.\d+)%", result_text).group(1))

        print ('body_fat', body_fat_value)
        if str(body_fat_value) == str(config['body_fat']):
            print ('Test case: Passed')
        else:
            print ('Test case: Not Passed')

    except Exception as e:
        print("Not appear result element:")
        print(f"Error result body fat: {e}")

    # Step 3: Return the extracted data
    return body_fat_value, status


def check_age_error_body(driver, config):
    # Validate age
    age = config['age']  # Default to 0 if 'age' key is missing
    if age<0 or age is None:
        # Check for error message
        time.sleep(1)  # Wait for the error message to potentially load
        try:
            error_message = driver.find_element(By.XPATH, "//div[font[@color='red']]")
            if "Please provide a positive age." in error_message.text:
                return True
            else:
                return False
        except:
            return False
    if age == 0:
        pass

def input_values_body_fat(driver, config):
    print("config", config)
    metric_link = driver.find_element(By.XPATH, '//a[contains(text(), "Metric Units")]')
    metric_link.click()

    age_input = driver.find_element(By.NAME, 'cage')
    age_input.clear()
    print("config['neck']", config['neck'])
    if config['age'] is not None:
        age_input.send_keys(config['age'])

    height_input = driver.find_element(By.NAME, 'cheightmeter')
    height_input.clear()
    if config['height'] is not None:
        height_input.send_keys(config['height'])


    weight_input = driver.find_element(By.NAME, 'cweightkgs')
    weight_input.clear() 
    if config['weight'] is not None:
        weight_input.send_keys(config['weight'])

    neck_input = driver.find_element(By.NAME, 'cneckmeter')
    neck_input.clear()
    if config['neck'] is not None:
        neck_input.send_keys(config['neck'])

    waist_input = driver.find_element(By.NAME, 'cwaistmeter')
    waist_input.clear() 
    if config['waist'] is not None:
        waist_input.send_keys(config['waist'])

    
    # Select gender based on config
    time.sleep(2)
        # Select gender based on config
    if config['gender'] == 'male':
        radio = driver.find_element(By.XPATH,"//label[contains(text(),'male')]")
        radio.click()
    elif config['gender'] == 'female':
        radio = driver.find_element(By.XPATH,"//label[contains(text(),'female')]")
        radio.click()
    else:
        print("Invalid gender specified in config")


    # Click on the "Calculate" button
    calculate_button = driver.find_element(By.XPATH, '//input[@value="Calculate"]')
    calculate_button.click()


    if (config['age'] is not None and config['age'] < 0) or config['age'] is None:
        age_flag = check_age_error_body(driver, config)
        print("age_flag", age_flag)

    if (config['height'] is not None and config['height'] < 0) or config['height'] is None:
        height_flag = check_height_error(driver, config, error = "Height need to be positive.")
        print("height_flag", height_flag)

    if (config['weight'] is not None and config['weight'] < 0) or config['weight'] is None:
        weight_flag = check_weight_error(driver, config)
        print("weight_flag", weight_flag)

    if (config['neck'] is not None and config['neck'] < 0) or config['neck'] is None:
        neck_flag = check_weight_error(driver, config, error = "Neck need to be numeric.")
        print("neck_flag", neck_flag)

    if (config['waist'] is not None and config['waist'] < 0) or config['waist'] is None:
        waist_flag = check_waist_error(driver, config, error = "Waist need to be numeric.")
        print("waist_flag", waist_flag)


    check_result_body_fat(driver, config)

driver.get("https://www.calculator.net/body-fat-calculator.html")

time.sleep(1)
for test_case in config['Body_fat_test']:
    try:
        print(f'\nTest for case: {test_case}')
        input_values_body_fat(driver, config['Body_fat_test'][test_case])
        time.sleep(2)
    except Exception as e:
        print(f"error: {e}")
    


time.sleep(10)
# Close the browser window
# driver.quit()
