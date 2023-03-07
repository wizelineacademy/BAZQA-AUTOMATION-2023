Feature: Log In

  Background:
    Given we are in the Home Page


    @e2e
    Scenario: login correct credentials
      Given we tap on the side menu
      And we tap on Log In
      When we enter the correct user
      And we enter the correct password
      And we tap on Login button
      Then the Home Page shows the Products label


