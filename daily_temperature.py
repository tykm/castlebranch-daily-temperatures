from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import time
import random

# Load username and password from .env
load_dotenv()

# Uses Chrome web driver to access web
driver = webdriver.Chrome('C:/Users/tyler/AppData/Roaming/Python/Python39/Scripts/chromedriver.exe')

# Open the login website
driver.get('https://login.castlebranch.com/login')

# Select username, password, login button
username_box = driver.find_element_by_id('username')
password_box = driver.find_element_by_id('password')
login_button = driver.find_element_by_xpath('//button[1]')

# Fill in user and pw boxes with credentials
username_box.send_keys(os.getenv('CB_USERNAME'))
password_box.send_keys(os.getenv('CB_PASSWORD'))

# Press login button
login_button.click()

# Wait for login page to load
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_xpath("//button[@class='button mx-2 unstyled-button']"))

# Locate and press dismiss button
dismiss_button = driver.find_element_by_xpath("//button[@class='button mx-2 unstyled-button']")
dismiss_button.click()

# Locate and press launch CB Bridges button
cb_bridges_button = driver.find_element_by_xpath("//button[@class='button mx-auto my-4 w-32 blue-button']")
cb_bridges_button.click()

# Wait for bridges page to load
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_xpath("//a[@class='wellness-enter px-4 py-2 center no-underline border border-transparent rounded self-stretch text-white bg-cb-blue hover:bg-blue-dark']"))

# Navigate to wellness center
driver.get('https://cbbridges.com/#wellness-center')

# Wait for wellness center page to load
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_xpath("//input[@value='5270021258413603424']"))

# Locate temperature and submit buttons
temperature_box = driver.find_element_by_id('temperature-reading')
submit_button = driver.find_element_by_xpath("//button[@class='temperature-submit bg-cb-blue text-white px-8 py-2 border rounded-lg bg-blue-light cursor-not-allowed']")

# Fill in temperature box with randomized temperature within acceptable range
temperature_box.send_keys(str(round(random.uniform(98.0, 98.8), 1)))

# Locate and fill in radio yes/no question buttons
radio_symptoms = driver.find_element_by_xpath("//input[@id='radio-symptoms-5270021258413603424']")
radio_contact_symptoms = driver.find_element_by_xpath("//input[@id='radio-contact.symptoms-5270021258413603424']")
radio_contact_exposed = driver.find_element_by_xpath("//input[@id='radio-contact.exposed-5270021258413603424']")
radio_travel = driver.find_element_by_xpath("//input[@id='radio-travel-5270021258413603424']")
radio_symptoms.click()
radio_contact_symptoms.click()
radio_contact_exposed.click()
radio_travel.click()

# Wait until radio buttons clicked
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_xpath("//button[@class='temperature-submit bg-cb-blue text-white px-8 py-2 border rounded-lg']"))

# Submit form
submit_button.click()

time.sleep(2)