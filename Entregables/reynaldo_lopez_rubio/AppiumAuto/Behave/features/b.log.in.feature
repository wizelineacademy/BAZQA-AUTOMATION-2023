Feature: Log In

  Background:
    Given we are in the Home Page

      @e2e
  Scenario: login_correct_credentials
      Given we tap on the side menu
        Then we tap on Log in
        And we enter the correct user
        And we enter the correct password
        And Tap on the Log In button



