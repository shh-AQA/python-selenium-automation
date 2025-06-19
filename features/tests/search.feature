# Created by szhuss at 6/19/25
Feature: Test cases for search field

  Scenario: Verify user can see product names and images
    Given Open target main page
    When  Input airpods into search field
    And Click on search icon
    Then Verify every product has a name and image