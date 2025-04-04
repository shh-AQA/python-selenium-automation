
Feature: Target search test cases


  Scenario: User can search for a product on Target.com
    Given Open target main page
    When User searches for product 'tea'
    Then Verify search results are shown and include 'tea'