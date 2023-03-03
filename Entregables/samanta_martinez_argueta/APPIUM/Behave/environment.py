import os
import shutil
from datetime import datetime
from appium import webdriver
from behave.model_core import Status
from os.path import dirname, abspath  # para leer la contraseña en .env
from dotenv import dotenv_values  # para leer la contraseña en .env


def desired_caps_setup(context):
    return {"platformName": "Android",
            "appium:platformVersion": "10",
            "appium:deviceName": "431662a1",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.saucelabs.mydemoapp.rn",
            "appium:appActivity": ".MainActivity"}


def context_variables(context):
    current_directory = dirname(abspath(__file__))  # para leer la contraseña en .env buscamos que se muestre la ubicación del archivo para sacar el path
    context.data = dotenv_values(f'{current_directory}/.env')  # para leer la contraseña en .env se le dice que se utilizará lo del archivo .env
    context.STANDARD_USER = context.data["STANDARD_USER"]  # para leer la contraseña en .env se le dice que al contexto se le agregue la variable que va a obtener de standard_user
    context.PASSWORD = context.data["PASSWORD"]  # para leer la contraseña en .env se le dice que al contexto se le agregue la variable que va a obtener de standard_user cada quien tendrá su archivo .env en su local
    userdata = context.config.userdata
    context.DRIVER_LOCATION = userdata.get('driver_location')
    context.PLATFORM = userdata.get("platform")
    context.PLATFORM_VERSION = userdata.get('platform_version')
    context.DEVICE_NAME = userdata.get("device_name")
    context.BUILD_NAME = userdata.get("build_name")
    context.ENVIRONMENT = userdata.get("environment")
    context.FEATURE = userdata.get("feature")
    context.TESTING_PROCESS = userdata.get("testing_process")
    context.PROGRAM = userdata.get("program")


def start_driver(context):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_setup(context))


def before_all(context):
    context_variables(context)


# scenario needs to be sent as param even though it is not used inside the function


def before_scenario(context, scenario):
    start_driver(context)
    context.driver.implicitly_wait(20)


def after_scenario(context, scenario): pass


def after_all(context): pass
