import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "Samsung S",
    "appium:automationName": "UiAutomator2",
    "appium:app": "E:\\Users\\72282\\Documents\\pruebasCurso.apk"
}

URL = "http://127.0.0.1:4723/wd/hub"

# Fixture. Define el driver.
@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
