Feature: Log in

  Background:
    Given we are in the Home Page

    @Regression
    Scenario: login_correct_credentials
      Given we tap on the side menu
      Then we tap on Log in
      And we enter the correct user
      And we enter the correct password
      And we tap on Log in button
      Then we are in the Home Page
