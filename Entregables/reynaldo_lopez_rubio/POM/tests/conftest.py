import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
    "platformName": "Android",
    "appium:platformVersion": "8.1",
    "appium:deviceName": "Prueba",
    "appium:automationName": "UiAutomator2",
    "appium:app": "E:/Users/1059769/Downloads/Android-MyDemoAppRN.1.3.0.build-244.apk"
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
