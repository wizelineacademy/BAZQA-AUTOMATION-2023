Feature: Screen My Cart

  Background:
    Given we are  in  the Home Page

@smoke
  Scenario: Add a product to the cart and validate product data
  Given   we tap on the product1
    Then  we tap on add car
    Then  we tap on cart badge
    Then  we see the Name Product1
    And  we see the Price Product1




