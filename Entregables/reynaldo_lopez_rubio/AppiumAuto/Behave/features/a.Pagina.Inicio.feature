Feature: Home Screen

Background:
  Given we are in the Home Page


  @e2e
  Scenario: validate_home_screen
    Then we see the products label
