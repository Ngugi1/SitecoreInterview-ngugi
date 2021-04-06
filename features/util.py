# Use predefined expected conditions e.g. when an element is clickable
from selenium.webdriver.support import expected_conditions as EC
# Import element location strategies e.g. find_element by By.Id
from selenium.webdriver.common.by import By
def show_traveller_settings(context):
  ''' Open traveller settings dialog'''

  # Find the path of the anchor to be clicked
  xpath = '//*[@id="adaptive-menu"]/a'
  # Wait for anchor to be clickable and click it.
  context.wait_driver.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

def search_flight_and_accommodation(context):
  ''' Search for flights and accommodation '''
  # We are trying to locate the button "Search" with xpath
  # Unfortunately, even with WebDriverWait the driver raises NoSuchElementException
  xpath_search_flights_and_accommodation = '/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/form/div[2]/div/button'
  # Wait for such button to be clickable and click it
  context.driver.find_element_by_xpath(xpath_search_flights_and_accommodation).click()
