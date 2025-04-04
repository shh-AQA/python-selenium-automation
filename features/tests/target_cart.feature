Feature: Target cart test case


  Scenario: Shopping cart is empty
    Given Open target main page
    When User clicks on shopping cart icon
    Then Verify 'Your cart is empty' message is shown