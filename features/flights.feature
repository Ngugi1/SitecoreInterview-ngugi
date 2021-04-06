Feature: Search for Brussels-New York flights on Expedia Website (US)

    Verify that there is at least one available flight - for an adult and a 3yr old child - from BRUSSELS
    to NEW YORK on expedia.com within the next three months.

  Scenario: Search for flights+accomodation on expedia.com
  Given I navigate to the Expedia website
  And I set Expedia website to be English US
  When I set travellers to be a 3yr old child and adult
  And I set choose a travel date within 3 months from today
  And I search for available flight (from Brussels to New York) + accommodation
  Then the result page contains travel option for the chosen destination
