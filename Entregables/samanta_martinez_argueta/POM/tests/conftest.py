import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
  "platformName": "Android",
  "appium:platformVersion": "10",
  "appium:deviceName": "Xiomi redmi note 9",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.saucelabs.mydemoapp.rn",
  "appium:appActivity": "com.saucelabs.mydemoapp.rn.MainActivity"
}

#DATA_PATH = "../utils/data.yml"

URL = "http://127.0.0.1:4723/wd/hub"

"""
# Función que lee el archivo yaml.
def load_data(path):
    with open(path) as data:
        return yaml.safe_load(data)


# Fixture. Carga el archivo con los datos.
@pytest.fixture(params=load_data(DATA_PATH))
def data(request):
    return request.param

"""
# Fixture. Define el driver.
@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver #regresa a la función después de usar driver y lo apaga con driver.quit
    driver.quit()
