from behave import *
from screens.home_screen import HomeScreen
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from utils.dictionaries.home_screen_texts import HOME_TEXTS
from utils.common_actions import CommonActions


@Step('we are in the Home Page') #se utiliza Step en este punto para que se adapte a lo que se requiera en el archivo feature pues es la misma validación pero al inicio es Given y al final Then
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


@When('we tap on Sauce Labs Bolt T-Shirt')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.img_bolt_product)


@Then('we tap on Shopping Cart')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.btn_shop_cart)

