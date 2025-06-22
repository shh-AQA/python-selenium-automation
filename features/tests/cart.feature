# Created by szhuss at 6/4/25
Feature: Test scenarios for Target shopping cart

  Scenario: Verify shopping cart is empty
    Given Open target main page
    When User clicks on shopping cart icon
    Then Verify message Your cart is empty is displayed
    Then Verify Cart Page opened
  
  
  Scenario: Verify correct item and item count has been added to cart
    Given Open target main page
    When Input mug into search field
    And Click on search icon
    And Click on product image
    And Store product name from product details page
    And Click on Add to Cart on product details page
    And User clicks on shopping cart icon in cart overlay
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product

