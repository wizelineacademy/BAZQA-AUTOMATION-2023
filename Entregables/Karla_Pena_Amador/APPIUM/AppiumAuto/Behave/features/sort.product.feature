Feature: Sort product
  Background:
    Given we are in the Home Page

    @regression_Test
    @e2e
    Scenario: sort_product_ascending
      Given we tap sort button
      Then we tap price-ascending

