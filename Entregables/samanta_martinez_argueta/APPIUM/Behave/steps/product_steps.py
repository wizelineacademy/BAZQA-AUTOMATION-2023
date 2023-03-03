from behave import *
from screens.product_screen import ProductDetail
from appium.webdriver.common.touch_action import TouchAction
from utils.common_actions import CommonActions
from utils.dictionaries.prod_texts import PROD_TEXTS


@When('we see the Product')
def step_impl(context):
    product_bolt = ProductDetail(context)
    product_bolt.find_element(*product_bolt.txt_name_product)


@When('we validate the Product Name')
def step_impl(context):
    product_bolt = ProductDetail(context)
    product_bolt.find_element(*product_bolt.txt_name_product)
    product_bolt.assert_text(*product_bolt.txt_name_product, text=PROD_TEXTS.get('txt_name_product'))


@When('we validate the Product Price')
def step_impl(context):
    product_bolt = ProductDetail(context)
    product_bolt.find_element(*product_bolt.txt_price_product)
    product_bolt.assert_text(*product_bolt.txt_price_product, text=PROD_TEXTS.get('txt_price_product'))


@Then('we tap on Add To Cart')
def step_impl(context):
    product_bolt = ProductDetail(context)
    product_bolt.tap_element(*product_bolt.btn_add_to_cart)
