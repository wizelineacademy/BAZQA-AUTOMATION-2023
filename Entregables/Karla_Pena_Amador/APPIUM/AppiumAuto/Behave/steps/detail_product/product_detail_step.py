from behave import *
from screens.detail_product.detail_product_screen import DetailProductScreen


@When('we tap in product')
def step_impl(context):
    detail_product = DetailProductScreen(context)
    detail_product.tap_element(*detail_product.btn_product)

@When('we tap Add To Cart button')
def step_impl(context):
    detail_product = DetailProductScreen(context)
    detail_product.tap_element(*detail_product.btn_add_car)


@When('we tap To cart badge')
def step_impl(context):
    detail_product = DetailProductScreen(context)
    detail_product.tap_element(*detail_product.btn_cart_badge)








