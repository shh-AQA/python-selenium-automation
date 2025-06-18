# Created by szhuss at 6/4/25
Feature: Test scenarios for Target shopping cart

  Scenario: Verify shopping cart is empty
    Given Open target main page
    When User clicks on shopping cart icon
    Then Verify message Your cart is empty is displayed
  
  
  Scenario: Verify correct item and item count has been added to cart
    Given Open target main page
    When Input hat into search field
    And Click on search icon
    And Click on product image
    And Store product name
    And Click on Add to Cart
    And Click on 'View Cart & checkout' button in side navigation
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

