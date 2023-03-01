import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:deviceName": "samsung SM-A525M",
    "appium:automationName": "UiAutomator2",
    "appium:app": "...\\TestApp.apk"
}

URL = "http://127.0.0.1:4723/wd/hub"


# Se define el driver.
@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
