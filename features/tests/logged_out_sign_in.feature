Feature: Sign In Test Case


  Scenario: Logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened