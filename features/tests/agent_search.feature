Feature: Test cases for homepage


  Scenario: User can log into Reelly
    Given Open Reelly login page
    When Input valid credentials
    And Click on login button
    And Click on market button
    And Filter market results for Agent
    Then Market results for Agent are shown