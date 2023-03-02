Feature: Detail Product
   Background:
    Given we are in the Home Page


  @smoke_Test
  @e2e
  Scenario: validate_detail_product_select
    When we tap in product
    When we tap Add To Cart button
    When we tap To cart badge
    Then we see to detail product name to select label
    And we see to detail product price
    When we tap Proceed To Checkout button
    When we enter the correct username to buy
    When we enter the correct password to buy
    When we tap button Login to buy
    When we enter the fullname
    When we enter the address
    When we enter the city
    When we enter the state
    When we enter the zipcode
    When we enter the country
    When we tap payment button
    When we enter the fullname to pay
    When we enter the card number
    When we enter the expiration date
    When we enter the security code
    When we tap review button



