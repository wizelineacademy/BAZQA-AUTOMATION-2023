Feature: Product Screen validation

  Background:
    Given we are  in  the Home Page

@regresion
  Scenario: Validate first product data (name and price)
  Given  we tap on the product1
    Then we see the Name Product
    And  we see the Price Product
    Then we swap screen





