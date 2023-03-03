Feature: Product detail

Background:
      Given we are in the Home Page

@e2e
Scenario: validate_product_detail
  When we tap on Sauce Labs Bolt T-Shirt
  And we see the Product
  And we validate the Product Name
  And we validate the Product Price
  Then we tap on Add To Cart
