import pytest
from appium import webdriver
from utils.Contants import Constants


CAPABILITIES = {
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "surya",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.swaglabsmobileapp",
    "appium:appActivity": ".MainActivity"
}


URL = "http://127.0.0.1:4723/wd/hub"


@pytest.fixture()
def constants():
    constants = Constants()
    return constants


@pytest.fixture()
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.implicitly_wait(wait_seconds)
    driver.quit()
