Feature: Checkout

  Background:
    Given we are in the Home Page
    When we tap on first product
    And we tap on Add To Cart
    And we see a number one on the Cart


  @regression
    Scenario: validate_check_out
      When we tap on the Cart
      And we tap on proceed to checkout
      And we enter the correct user
      And we enter the correct password
      And tap on the Log In button
      And we enter the full name
      And we enter the address
      And we enter the city
      And we enter the zip code
      And we enter the country
      And we tap to payment
      And we enter the buyer full name
      And we enter the card number
      And we enter the expiration date
      And we enter the security code
      And we tap on review order
      And we tap on place order
      Then we see the checkout complete
      And we tap the Continue Shopping