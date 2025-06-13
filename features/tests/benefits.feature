# Created by szhuss at 6/12/25
Feature: Verify benefits for Target Circle

  Scenario: There are at least 10 benefit cells displayed
    Given Open target circle page
    Then Verify at least 10 benefit cells are displayed
