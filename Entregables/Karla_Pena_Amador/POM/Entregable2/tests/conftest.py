import pytest
from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "b2q",
    "appium:automationName": "UiAutomator2",
    "appium:app": "e:\\Users\\88433\\Downloads\\appPrueba.apk",
    "appium:appPackage": "com.saucelabs.mydemoapp.rn",
    "appium:appActivity": ".MainActivity"
}

URL = "http://127.0.0.1:4723/wd/hub"


@pytest.fixture
def driver():
    wait_seconds = 30
    driver = webdriver.Remote(URL, desired_capabilities)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
