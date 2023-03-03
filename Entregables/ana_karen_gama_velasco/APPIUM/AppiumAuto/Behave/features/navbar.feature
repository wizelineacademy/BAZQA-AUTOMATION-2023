Feature: Cart Screen

  Background:
    Given we are in the Home Page

  @regression
  Scenario: validate_order_by_price_asc
    When we tap on sort by
    And we select price asc option
    Then we see the products in asc order 