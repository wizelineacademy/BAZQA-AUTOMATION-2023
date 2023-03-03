Feature: Home Screen

  Background:
    Given we are in the Home Page

  @smoke
    @regression
  Scenario: validate_home_screen
    Then we see the Products label

