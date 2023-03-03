import time

from behave import *
from screens.checkout.checkout_screen import CheckOutScreen
from utils.dictionaries.checkout_screen_texts import *


@When('we enter the full name')
def step_impl(context):
    time.sleep(2.4)
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_full_name, text=FULL_NAME.get("FULL_NAME"))


@When('we enter the address')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_address, text=ADDRESS.get("ADDRESS"))


@When('we enter the city')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_city, text=ADDRESS.get("CITY"))


@When('we enter the zip code')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_zip_code, text=ADDRESS.get("ZIP_CODE"))


@When('we enter the country')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_country, text=ADDRESS.get("COUNTRY"))


@When('we tap to payment')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.tap_element(*chout_screen.btn_to_payment)

