from behave import *
from screens.detail_product_screen import DetailProduct
from utils.dictionaries.detail_product_screen_texts import DETAIL_TEXTS


@When('we select the product')
def step_impl(context):
    detail_product = DetailProduct(context)
    detail_product.tap_element(*detail_product.store_item)


@Step('we see the product detail')
def step_impl(context):
    detail_product = DetailProduct(context)
    detail_product.find_element(*detail_product.name_product)
    detail_product = DetailProduct(context)
    detail_product.find_element(*detail_product.price)


@Then('we add to the cart')
def step_impl(context):
    detail_product = DetailProduct(context)
    detail_product.tap_element(*detail_product.add_car)
    detail_product = DetailProduct(context)
    detail_product.tap_element(*detail_product.card_badge)
    detail_product = DetailProduct(context)
    detail_product.find_element(*detail_product.my_cart)
    detail_product = DetailProduct(context)
    detail_product.assert_test(*detail_product.check_product, text=DETAIL_TEXTS.get('check_product'))
    detail_product = DetailProduct(context)
    detail_product.assert_test(*detail_product.check_price, text=DETAIL_TEXTS.get('check_price'))
