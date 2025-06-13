# Created by szhuss at 6/12/25
Feature: Test case for Target Help UI

  Scenario Outline: Verify elements are present on UI
    Given Open Target Help page
    Then Verify <UI element>
    Examples:
    |UI element                             |
    |Target Help header                     |
    |search help input field                |
    |search button                          |
    |What would you like to do section      |
    |contact us and product recalls section |
    |Browse all help pages text             |