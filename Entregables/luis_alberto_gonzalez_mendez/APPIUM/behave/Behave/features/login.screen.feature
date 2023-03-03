Feature: Login Screen

    @regression
    Scenario: Successful login
      Given I am on the login screen
      When I enter my valid credentials
      And I tap the login button
      Then you should be redirected to the products screen
