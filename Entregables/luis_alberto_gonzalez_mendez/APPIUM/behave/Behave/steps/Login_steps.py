from behave import *
from screens.Login_screen import LoginScreen
from utils.dictionaries.login_screen_text import HOME_TEXTS, USUARIOS
from utils.common_actions import CommonActions


@Given('I am on the login screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.find_element(*login_screen.login_screen)

@When('I enter my valid credentials')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.enter_text(*login_screen.username_input, text=USUARIOS.get("USERNAME"))
    login_screen.enter_text(*login_screen.password_input, text=USUARIOS.get("PASSWORD"))

@When('I tap the login button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.find_and_click_element(*login_screen.login_button)

@Then('you should be redirected to the products screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.assert_text(*login_screen.home_page, text=HOME_TEXTS.get('HOME_PAGE'))
