Feature: Add Cart

  Background:
    Given we are in the Home Page
    Given we select a product

    @e2e
    Scenario: select any product
      Given we select a product
      When we validate the name of the product
      And we validate the price of the product
      And we tap on Add to Cart
      Then the cart badge shows an added product


    @e2e
    Scenario: validate product in cart
      Given we tap a product
      And we Add to Cart
      And we tap my cart
      When we validate the image
      And we validate the name label
      And we validate the price label
      And we validate the color
      Then the button Proceed To Checkout is available