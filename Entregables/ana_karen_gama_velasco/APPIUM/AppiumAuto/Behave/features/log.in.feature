Feature: Log In

  Background:
    Given we are in the Home Page

  @smoke
    @regression
  Scenario: login_correct_credentials
    Given we tap in the side menu
    When we tap on Log In
    And we enter the correct user
    And we enter the correct password
    And tap on the Log In button
    Then we are in the Home Page

