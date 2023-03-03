from behave import *
from screens.Price_filter_screen import PriceFilter
from utils.common_actions import CommonActions
from utils.dictionaries.price_filter_text import PRICE_FILTER


@Given('you tapped on the sort filter')
def step_impl(context):
    Price_Filter = PriceFilter(context)
    Price_Filter.find_and_click_element(*Price_Filter.tap_filter)


@When('I select the option Price from lowest to highest')
def step_impl(context):
    Price_Filter = PriceFilter(context)
    Price_Filter.find_and_click_element(*Price_Filter.price_filter)


@When('we validate the product with the least')
def step_impl(context):
    Price_Filter = PriceFilter(context)
    Price_Filter.assert_text(*Price_Filter.lower_price, text='$7.99')


@When('scroll on the screen')
def step_impl(context):
    Price_Filter = PriceFilter(context)
    Price_Filter.scroll(*Price_Filter.name_product)


@Then('we validate the product with the highest price')
def step_impl(context):
    Price_Filter = PriceFilter(context)
    Price_Filter.assert_text(*Price_Filter.higher_price, text='$49.99')
