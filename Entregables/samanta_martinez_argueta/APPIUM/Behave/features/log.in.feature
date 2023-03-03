Feature: Log In


Background:
  Given we are in the Home Page

 @e2e
 Scenario: login_correct_credentials
   Given we tap on the side menu
   Then we tap on log in
   And we enter the correct user
   And we enter the correct password
   And we tap on the button login
   Then we are in the Home Page