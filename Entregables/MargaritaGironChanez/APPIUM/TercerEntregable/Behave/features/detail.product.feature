Feature: Detail product

  Background:
    Given we are in the Home Page

    @e2e @Regression
    Scenario: validate_the_detail_product
      When we select the product
      Then we see the product detail
      And we add to the cart