from behave import *
from screens.home_screen import HomeScreen
from utils.dictionaries.home_screen_texts import HOME_TEXTS
from utils.common_actions import CommonActions


@Given('we are in the Home Page')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_element(*home_screen.lbl_products)


@Then('we see the Products label')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_products, text=HOME_TEXTS.get('lbl_products'))


@Given('we tap on the side menu')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.menu_side)


@Then('the Home Page shows the Products label')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_product, text=HOME_TEXTS.get('lbl_product'))


@Given('we tap on sort button')
def step_impl(context):
    sort_screen = HomeScreen(context)
    sort_screen.tap_element(*sort_screen.btn_sort)


@When('we tap on Price Ascending option')
def step_impl(context):
    price_ascend = HomeScreen(context)
    price_ascend.tap_element(*price_ascend.lbl_ascending)


@Then('the first price is the lowest')
def step_impl(context):
    first_price = HomeScreen(context)
    first_price.assert_text(*first_price.lbl_lwprice, text=HOME_TEXTS.get('lbl_lwprice'))