from behave import *
from screens.detail_product.card_badge_screen import CardBadgeScreen
from utils.dictionaries.detail_product_texts import DETAIL_PRODUCT_TEXTS


@Then('we see to detail product name to select label')
def step_impl(context):
    card_badge = CardBadgeScreen(context)
    card_badge.assert_text(*card_badge.lbl_product_name, text=DETAIL_PRODUCT_TEXTS.get('lbl_product_name'))


@Then('we see to detail product price')
def step_impl(context):
    card_badge = CardBadgeScreen(context)
    card_badge.assert_text(*card_badge.lbl_product_price, text=DETAIL_PRODUCT_TEXTS.get('lbl_product_price'))


@When('we tap Proceed To Checkout button')
def step_impl(context):
    card_badge = CardBadgeScreen(context)
    card_badge.tap_element(*card_badge.btn_Proceed_To_Checkout)