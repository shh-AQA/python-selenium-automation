# Created by szhuss at 6/4/25
Feature: Test scenarios for Target shopping cart

  Scenario: Verify shopping cart is empty
    Given Open target main page
    When User clicks on shopping cart icon
    Then Verify message Your cart is empty is displayed


Scenario: A product is added to cart
  Given Open target main page
  When Input chocolate into search field
  And Click on search icon
  And Click on Add to Cart
  And Click on Add to Cart in side navigation
  Then Verify product is added to shopping cart