from behave import *
from screens.detail_product.log_in_buy_screen import LoginScreenBuy



# aunque en el feature este and en los pasos se agrega then
@When('we enter the correct username to buy')
def step_impl(context):
    log_in = LoginScreenBuy(context)
    # log_in.fill_text(*log_in.txt_username, text=LOGIN_TEXTS.get('txt_username'))
    log_in.fill_text(*log_in.txt_username_to_buy, text=context.STANDARD_USER)


@When('we enter the correct password to buy')
def step_impl(context):
    log_in = LoginScreenBuy(context)
    # log_in.fill_text(*log_in.txt_password, text=LOGIN_TEXTS.get('txt_password'))
    log_in.fill_text(*log_in.txt_password_to_buy, text=context.PASSWORD)


@When('we tap button Login to buy')
def step_impl(context):
    log_in = LoginScreenBuy(context)
    log_in.tap_element(*log_in.btn_login_to_buy)
