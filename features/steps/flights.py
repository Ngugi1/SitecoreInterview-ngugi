from behave import *
import unittest
import time
from selenium.webdriver.common.keys import Keys
# Use predefined expected conditions e.g. when an element is clickable
from selenium.webdriver.support import expected_conditions as EC
# Import element location strategies e.g. find_element by By.Id
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


DEFAULT_TIMEOUT = 10
@given('I navigate to the Expedia website')
def step_impl(context):
  context.driver.get("https://expedia.com")
  assert "Expedia" in context.driver.title


@given('I set Expedia website to be English US')
def step_impl(context):
  # Set USA as region
  context.preference.set_region(context)
  context.preference.set_language(context)
  context.preference.save_language_region_preferebces(context)

@when('I set travellers to be a 3yr old child and adult')
def step_impl(context):
  context.util.show_traveller_settings(context)
  context.preference.set_adult_traveller(context)
  context.preference.set_child_traveller(context)
  context.preference.set_child_age(context)
  # #  Confrirm that correct adult and child values are set
  assert int(context.driver.find_element_by_id("adult-input-0").get_attribute('value')) == 1
  assert int(context.driver.find_element_by_id("child-input-0").get_attribute('value')) == 1


@when('I set choose a travel date within 3 months from today')
def step_impl(context):
  '''Pass this test by default - default date is withing the provided range'''
  pass


@when('I search for available flight (from Brussels to New York) + accommodation')
def step_impl(context):
  context.preference.set_destination(context)
  context.preference.include_flight(context)
  context.preference.set_origin(context)
  context.util.search_flight_and_accommodation(context)


@then('the result page contains travel option for the chosen destination')
def step_impl(context):
  # Find the unordered list containing search results
  available_search_results = context.wait_driver.until(EC.visibility_of_element_located((By.CLASS_NAME, "results-list no-bullet")))
  # Confirm the list has at least one element
  assert len(context.driver.find_elements_by_xpath('//*[@id="app-layer-base"]/div/div/div/div[1]/main/div[3]/div/div[2]/section[2]/ol/li')) > 0
