import time

from behave import *
from screens.home_screen import HomeScreen
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

from utils.dictionaries.home_screen_texts import HOME_TEXT


@Step('We are in the Home Page')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_element(*home_screen.lbl_products)


@Then("We see the Products label")
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_products, text=HOME_TEXT.get('lbl_products'))


@Given('we tap in the side menu')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.menu_side)


@When('we tap on first product')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.first_product)


@When('we tap on sort by')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.btn_sort)


@Then('we see the products in asc order')
def step_impl(context):
    time.sleep(2.4)
    home_screen = HomeScreen(context)
    first_product = home_screen.find_element(*home_screen.lbl_price_first_product).text
    home_screen.driver.swipe(150, 400, 150, -800, 1000)
    last_product = home_screen.find_element(*home_screen.lbl_price_last_product).text
    fp_noprice_convert = first_product.replace('$', '')
    lp_noprice_convert = last_product.replace('$', '')
    compare_price_asc = float(fp_noprice_convert) < float(lp_noprice_convert)
    assert compare_price_asc
