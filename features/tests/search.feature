# Created by szhuss at 6/19/25
Feature: Test cases for search field

  Scenario: Verify user can search for shoes
    Given Open target main page
    When  Input shoes into search field
    Then Verify search worked for shoes

  Scenario: Verify user can search for mug
    Given Open target main page
    When  Input mug into search field
    Then Verify search worked for mug

  Scenario: Verify user can see product names and images
    Given Open target main page
    When  Input airpods into search field
    And Click on search icon
    Then Verify every product has a name and image

  Scenario: Tooltip displayed when user hovers over 'add to favorites' icon
    Given Open target main page
    When Input tea into search field
    And Click on search icon
    And Hover over 'add to favorites' icon
    Then Verify tooltip is displayed