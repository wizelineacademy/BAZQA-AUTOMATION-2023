from os.path import dirname, abspath
from appium import webdriver
from dotenv import dotenv_values

def desired_caps_setup(context):
    return {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "b2q",
        "appium:automationName": "UiAutomator2",
        "appium:app": "e:\\Users\\88433\\Downloads\\appPrueba.apk",
        "appium:appPackage": "com.saucelabs.mydemoapp.rn",
        "appium:appActivity": ".MainActivity"

    }

def context_variables(context):
    current_directory = dirname(abspath(__file__)) #DONDE SE ENCUENTRA UBICADO EL AARCHIVO
    context.data = dotenv_values(f'{current_directory}/.env') #obteniendo la información
    context.STANDARD_USER = context.data['STANDARD_USER'] #al contexto agregar una variable que almacena el  user
    context.PASSWORD = context.data['PASSWORD']#al contexto agregar una variable que almacena el  password
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
def after_scenario(context, scenario):
  pass
def after_all(context):
    pass