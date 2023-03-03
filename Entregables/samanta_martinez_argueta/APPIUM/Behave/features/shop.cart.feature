Feature: Shopping Cart

Background:
    Given we are in the Home Page
    Then we see the Products label
    When we tap on Sauce Labs Bolt T-Shirt
    Then we tap on Add To Cart

@e2e
Scenario: validate_product_in_the_shopping_cart
    When we tap on Cart
    Then we see the Shopping Cart
    And we validate the Product Name Added
    And we validate the Product Price Added
