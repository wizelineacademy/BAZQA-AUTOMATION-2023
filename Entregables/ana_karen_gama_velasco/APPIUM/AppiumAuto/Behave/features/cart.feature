Feature: Cart Screen

  Background:
    Given we are in the Home Page

  @smoke
    @regression
  Scenario Outline: validate_add_to_cart
    When we tap on first product
    And we tap on Add To Cart
    And we see a number one on the Cart
    And we tap on the Cart
    Then we validate products name "<name_product>"
    And we validate products price "<price_product>"
    Examples:
      | name_product        | price_product |
      | Sauce Labs Backpack | $29.99        |