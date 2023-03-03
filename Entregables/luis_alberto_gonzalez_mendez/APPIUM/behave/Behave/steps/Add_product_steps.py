from behave import *
from screens.Login_screen import LoginScreen
from screens.Add_product_screen import AddProduct
from utils.dictionaries.add_product_text import ADD_PRODUCT

@Given('the user has added a product to the cart')
def step_impl(context):
    add_product = AddProduct(context)
    add_product.find_and_click_element(*add_product.add_product)

@When('the user selects the "view cart" option')
def step_impl(context):
    add_product = AddProduct(context)
    add_product.find_and_click_element(*add_product.tap_car)

@Then('the user should see the product in the cart')
def step_impl(context):
    add_product = AddProduct(context)
    add_product.assert_text(*add_product.price_product, text=ADD_PRODUCT.get("PRICE_PRODUCT"))
    add_product.assert_text(*add_product.name_product, text=ADD_PRODUCT.get("NAME_PRODUCT"))
