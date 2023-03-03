from screens.side_menu.log_in_screen import LogInScreen
from behave import *
# from utils.dictionaries.detail_product_screen_texts import LOGIN_TEXTS


@Then('we enter the correct user')
def step_impl(context):
    log_in = LogInScreen(context)
    #log_in.fill_text(*log_in.txt_username, text="bob@example.com")
    #log_in.fill_text(*log_in.txt_username, text=LOGIN_TEXTS.get('txt_username'))
    log_in.fill_text(*log_in.txt_username, text=context.STANDARD_USER)


@Then('we enter the correct password')
def step_impl(context):
    log_in = LogInScreen(context)
    #log_in.fill_text(*log_in.txt_password, text=LOGIN_TEXTS.get('txt_password'))
    log_in.fill_text(*log_in.txt_password, text=context.PASSWORD)


@Then('we tap on Log in button')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.tap_element(*log_in.btn_login)


@Then('we tap on the Bold T-Shirt')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.tap_element(*log_in.store_item)
