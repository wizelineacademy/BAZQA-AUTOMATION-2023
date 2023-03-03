Feature: Home Screen

  Background:
    Given we are in the Home Page
    When we tap on first product


  @smoke
    @regression
  Scenario Outline: validate_product_price_and_name
    Then we see the Products name "<name>"
    And we see the Products price "<price>"
    Examples:
      | name                | price  |
      | Sauce Labs Backpack | $29.99 |




