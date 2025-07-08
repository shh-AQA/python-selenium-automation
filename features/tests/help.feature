# Created by szhuss at 6/12/25
Feature: Test case for Target Help UI

  Scenario Outline: Verify elements are present on UI
    Given Open Target Help page
    Then Verify <UI element>
    Examples:
    |UI element                               |
    |Target Help header                       |
    |search help input field                  |
    |search button                            |
    |What would you like to do section        |
    |contact us and product recalls section   |
    |Browse all help pages text is displayed  |

  Scenario: User can select Help topic 'Promotions and Coupons'
    Given Open Help Page for returns
    Then Verify help returns page opened
    When Select help topic Promotions & Coupons
    Then Verify help current promotions page opened
