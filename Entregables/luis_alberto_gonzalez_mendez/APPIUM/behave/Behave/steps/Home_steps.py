from behave import *
from screens.Home_screen import HomeScreen
from screens.Login_screen import LoginScreen
from utils.dictionaries.login_screen_text import USUARIOS
from utils.dictionaries.home_steps_text import PRODUCT_DETAIL

@step('login')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.enter_text(*login_screen.username_input, text=USUARIOS.get("USERNAME"))
    login_screen.enter_text(*login_screen.password_input, text=USUARIOS.get("PASSWORD"))
    login_screen.find_and_click_element(*login_screen.login_button)

@Given('the user makes tap in the button of a product')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_and_click_element(*home_screen.tap_product)

@Then('must be shown the product detail')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.product_price, text=PRODUCT_DETAIL.get("PRICE_PRODUCT"))
    home_screen.assert_text(*home_screen.product_name, text=PRODUCT_DETAIL.get("NAME_PRODUCT"))
