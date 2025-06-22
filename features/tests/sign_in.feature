# Created by szhuss at 6/4/25
Feature: Target Sign In test cases

  Scenario: Sign in form opens from side navigation
    Given Open target main page
    When User click on Account icon
    And User clicks on Sign in or create account button in login modal
    Then Verify sign in form is displayed