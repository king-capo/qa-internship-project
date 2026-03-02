Feature: Test cases for homepage


  Scenario: User can log into Reelly
    Given Open Reelly login page
    When Input valid credentials
    And Click on login button
    Then User is on Reelly homepage


  Scenario: User can filter market results for Agent
    Given Open Reelly main page
    When Click on market button
    And Verify market page is open
    And Filter market results for Agent
    Then Market results for Agent are shown