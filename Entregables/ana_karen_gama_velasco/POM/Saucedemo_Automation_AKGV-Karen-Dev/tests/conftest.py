import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "PixelXL",
  "appium:automationName": "UiAutomator2",
  "appium:app": "ruta donde se encuentre la apk"
}

URL = "http://0.0.0.0:4723/wd/hub"


@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
