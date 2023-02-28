import pytest
from dotenv import dotenv_values
from appium import webdriver

DESIRED_CAPABILITIES = {
  "appium:deviceName": "Pixel 4",
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:app": "/pythonProject/APP/saucedemo.apk"
}

DATA_PATH = "./utils/data.yml"

URL = "http://127.0.0.1:4723/wd/hub"

@pytest.fixture
def data():
    return dotenv_values("E:\DialerAutomationTest\.env")

# Fixture. Define el driver.
# este siempre teniamos que tenernos
@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()

