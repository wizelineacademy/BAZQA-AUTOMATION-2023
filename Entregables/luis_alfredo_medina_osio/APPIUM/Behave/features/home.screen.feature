Feature: Home Screen

  Background:
    Given we are in the Home Page

  @e2e
  Scenario: validate home screen
    Then we see the Products label

  @e2e
  Scenario: sort products
    Given we tap on sort button
    When we tap on Price Ascending option
    Then the first price is the lowest