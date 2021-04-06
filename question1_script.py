# Import selenium webdriver - enables us to control a browser
from selenium import webdriver

# Import element location strategies e.g. find_element by By.Id
from selenium.webdriver.common.by import By

# WebDriverWait wraps a normal driver but allows us to wait for some conditions to be true
from selenium.webdriver.support.ui import WebDriverWait

# Use predefined expected conditions e.g. when an element is clickable
from selenium.webdriver.support import expected_conditions as EC

# Default wait time
WAIT_TIMEOUT = 15

def duck_duck_go_search(keyword):
  ''' Search for a keyword on duckduckgo
      and take screenshot of the results page 
  '''

  # Instantiate chrome driver
  chrome_driver = webdriver.Chrome("/Users/ngugi/Downloads/chromedriver")
  try:
   # Use the driver to control the browser
    chrome_driver.get("https://duckduckgo.com")
    # Wait for WAIT_TIMEOUT seconds to try locate duckduckgo search box
    search_text_box = WebDriverWait(chrome_driver, WAIT_TIMEOUT).until(
      EC.presence_of_element_located((By.ID, "search_form_input_homepage")))

    # Input the search term on the search textbox
    search_text_box.send_keys(keyword)
    search_button = chrome_driver.find_element_by_id("search_button_homepage")
    # Click the search button
    search_button.click()
    # Find div with ID "links", it contains search results
    results_links_div = WebDriverWait(chrome_driver, WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, "links")))
    # Verify there is at least one result
    first_result = WebDriverWait(chrome_driver, WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, "r1-0")))
    # Ensure results are not empty
    assert first_result is not None
    # Take screenshot
    results_page = chrome_driver.find_element_by_class_name("body--serp")
    #  Take screenshot of results page
    chrome_driver.save_screenshot("screenshots/{0}-result-page.png".format(keyword))
  except Exception as ex:
    # Output error message
    print("Error: {}".format(str(ex)))
  finally:
    # Quit the browser window
    chrome_driver.quit()


# Search and take screenshot for Bahamas
duck_duck_go_search("Bahamas")
# Search and take screenshot for Amsterdam
duck_duck_go_search("Amsterdam")
# See results in ./screenshots/