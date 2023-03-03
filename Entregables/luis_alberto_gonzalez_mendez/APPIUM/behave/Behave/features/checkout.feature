Feature: Make a purchase

Background:
      Given login

      @e2e
      Scenario: Complete purchase
        Given the user has added multiple items to the shopping cart
        When the user selects the cart option
        And the purchase confirmation screen is displayed
        And customer data is entered
        And I tap the continue button
        And we scroll to find the button
        Then you should be redirected to the order processed screen