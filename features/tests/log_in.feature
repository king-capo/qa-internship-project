Feature: User login

  Scenario: User can log into Reelly
    Given Open Reelly login page
    When Input valid credentials
    And Click on login button
    Then User is on Reelly homepage

