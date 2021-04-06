# Selenium webdriver - helps control the browser
from selenium import webdriver
# WebDriverWait wraps a normal driver but allows us to wait for some conditions to be true
from selenium.webdriver.support.ui import WebDriverWait
# Import user preferences
import preference as preference
import util as util

def before_scenario(context, scenario):
    # Use context to keep reference to the web driver
    context.driver = webdriver.Chrome("/Users/ngugi/Downloads/chromedriver")
    # Maximize chrome window
    context.driver.maximize_window()
    # Use WebDriverWait to allow us to wait for 
    # desired contidions to evaluate to true or false
    context.wait_driver = WebDriverWait(context.driver, 10)
    # Store helpers inside the context 
    context.preference = preference
    context.util = util

def after_scenario(context, scenario):
    # Quit browser window when finished
    context.driver.quit()
