Feature: Home Screen

  Background:
    Given we are in the Home Page

  @e2e
  Scenario: order_by_price
    Given we are in the Home Page
    When we tap on the filter
    Then we see the products order by price
