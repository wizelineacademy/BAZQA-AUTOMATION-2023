Feature: add product to shopping cart

Background:
      Given login

      @regression
      Scenario: View product in cart
        Given the user has added a product to the cart
        When the user selects the "view cart" option
        Then the user should see the product in the cart