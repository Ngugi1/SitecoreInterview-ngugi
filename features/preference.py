# WebDriverWait wraps a normal driver but allows us to wait for some conditions to be true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# Use predefined expected conditions e.g. when an element is clickable
from selenium.webdriver.support import expected_conditions as EC
# Import element location strategies e.g. find_element by By.Id
from selenium.webdriver.common.by import By


def set_region(context, region=1):
    ''' Set user preffered region, default region '''

    # Click the button to allow you to switch languages
    # This step is necessary if someone's default driver language is not EN-US
    context.wait_driver.until(
      EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#secondaryNav > button"))
        ).click()

    # Select region - USA
    site_selector = Select(context.wait_driver.until(EC.element_to_be_clickable((By.ID, "site-selector"))))
    # USA corresponds to value 1
    site_selector.select_by_value(str(region))


def set_language(context, language=1033):
    ''' Set default language to be English'''

    # Select language - corresponds to value 1033 in the drop down
    language_selector = Select(context.wait_driver.until(
      EC.element_to_be_clickable(
        (By.ID, "language-selector"))))
    # Choose English language
    language_selector.select_by_value(str(1033))


def save_language_region_preferebces(context):
    # Find xpath of save button to keep region + language preferences
    # The disadvantage of using xpath is if page elements are reorganized, 
    # xpath might become invalid. However, we use it for lack of more appropriate
    # way to locate the element
    save_btn_xpath = '//*[@id="app-layer-disp-settings-picker"]/div[2]/div/div[3]/div[4]/button'
    # Click button whose xpath is save_btn_xpath to save user preferences
    context.wait_driver.until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()


def set_child_traveller(context):
  # Set the number of child travellers to one.
  # We use the strategy of using the provided buttons
  # to set the correct number of travellers
  no_of_default_child_travellers = int(context.driver.find_element_by_id("child-input-0").get_attribute('value'))
  if no_of_default_child_travellers > 1:
    #  Reduce no. of travellers to one, use the provided buttons
     for _ in range(no_of_default_child_travellers - 1):
       context.find_element_by_xpath('//*[@id="adaptive-menu"]/div/div/section/div[1]/div[3]/div/button[1]').click()
  elif no_of_default_child_travellers < 1:
    #  If no. of child travellers is zero, click appropriate button
    # to set it to 1
       context.driver.find_element_by_xpath('//*[@id="adaptive-menu"]/div/div/section/div[1]/div[3]/div/button[2]').click()


def set_adult_traveller(context):
  ''' Set number of adult travellers '''
  # Find the default value
  no_of_default_adult_travellers = int(context.driver.find_element_by_id("adult-input-0").get_attribute('value'))
  #  If number of defult adult traveller is greater than 1
  if no_of_default_adult_travellers > 1:
    #  Get reference to buttons to reduce and add number of adult travellers
     xpath_btn_reduce_adult_travellers = '//*[@id="adaptive-menu"]/div/div/section/div[1]/div[2]/div/button[1]'
     xpath_btn_add_adult_travellers = '//*[@id="adaptive-menu"]/div/div/section/div[1]/div[2]/div/button[2]'
    #  Reduce number of travellers to 1 by clicking
    # the reducing button no_of_default_adult_travellers - 1
     for _ in range(no_of_default_adult_travellers - 1):
      context.wait_driver.until(EC.presence_of_element_located((By.XPATH, xpath_btn_reduce_adult_travellers))).click()
  elif no_of_default_adult_travellers < 1:
    #  If no of adult travellers is less than 1, click it once to set 
    #  1 as no. of adult travellers
       xpath_btn_add_adult_travellers.click()


def set_child_age(context):
  # Set the age of the child
  # Select the child-age-input-0-0 selector
  select = Select(context.wait_driver.until(EC.visibility_of_element_located((By.ID, "child-age-input-0-0"))))
  # USA corresponds to value 1
  select.select_by_value("4")


def set_destination(context, destination="New York"):
  # To focus on the destination_field, first click the button overlaying it
  xpath = '//*[@id="location-field-destination-menu"]/div[1]/button'
  context.wait_driver.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
  # Find the destination_field
  destination_field = context.wait_driver.until(EC.visibility_of_element_located((By.ID, "location-field-destination")))
  # Set the destination
  destination_field.send_keys(destination)
  # Send enter command to finish setting destination
  destination_field.send_keys(Keys.RETURN)


def include_flight(context):
  ''' Include a flight for your stay '''

  # See if flight is already added, if not add it.
  # This makes origin text field to be visible
  if not context.driver.find_element_by_id("add-flight-switch").is_selected():
    # Force click with JS, element.click() doesn't  work sometimes
    add_flight_checkbox = context.driver.find_element_by_id("add-flight-switch")
    context.driver.execute_script("arguments[0].click();", add_flight_checkbox)

def set_origin(context, origin="Brussels"):
  ''' Set brussels as origin of flight '''
  # find button overlaying origin field 
  selector = '#location-field-origin-menu > div.uitk-field.has-floatedLabel-label.has-icon.has-no-placeholder > button'
  # Focus on origin field by clicking on it
  button_origin = context.driver.find_element_by_css_selector(selector)
  # click the it to  focus on origin field
  context.driver.execute_script("arguments[0].click();", button_origin)
  # Set origin
  location_field_origin = context.driver.find_element_by_id("location-field-origin")
  location_field_origin.send_keys("Brussels")
  # Finish setting origin
  location_field_origin.send_keys(Keys.RETURN)



