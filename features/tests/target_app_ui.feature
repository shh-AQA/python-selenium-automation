# Created by szhuss at 6/23/25
Feature: Test cases for Target UI app

  Scenario: User is able to open Privacy Policy link
    Given Open Target App page
    And Store original window
    When Click on Privacy Policy link
    And Switch to new window
    Then Verify Privacy Page opened
    Then Close current window
    Then Return to original window