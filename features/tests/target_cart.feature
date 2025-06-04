# Created by szhuss at 6/4/25
Feature: Test scenarios for Target shopping cart

  Scenario: Verify shopping cart is empty
    Given Open target main page
    When User clicks on shopping cart icon
    Then Verify message Your cart is empty is displayed


