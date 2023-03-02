<p align="center">
  <img width="600" height="200" src="https://huloop.ai/wp-content/uploads/2022/10/wizeline-logo-vert.svg">
</p>

# Proyecto POM en Python 🐍
Este proyecto es un ejemplo de cómo utilizar APPIUM, Python y POM para realizar pruebas moviles en la app de saucedemo. 

## Autor 🙍‍♂️
 - Luis Alberto González Méndez

## Dependencias 🔧

Para poder ejecutar este proyecto, necesitarás instalar las siguientes dependencias:

- Python
- Appium-Python-Client
- Selenium
- Pytest
- Flake8
- PyYAML
- Allure-pytest

Para instalar estas dependencias, puedes utilizar el siguiente comando:

````
pip install -r requirements.txt
````
## Configuración ⚙️

Antes de ejecutar las pruebas, debe configurar Appium y un dispositivo físico móvil en el que se ejecutará la aplicación de saucedemo.

1. Descargue e instale Appium.
2. Conecte su dispositivo móvil al ordenador mediante un cable USB.
3. Habilite la depuración USB en su dispositivo móvil. Para hacerlo, siga los pasos específicos para su dispositivo móvil y versión de Android.
4. Configure la capacidad de Appium en el archivo config.json. Asegúrese de que las capacidades platformName, deviceName, platformVersion, appPackage y appActivity estén configuradas correctamente.

## Estructura de Carpetas del Proyecto 📂
````
ProyectoPOMPython/
├── reports/
├── screens/
│     ├── __init__.py
│     ├── BaseScreen.py
│     ├── LoginPage.py
├── test/
│     ├── __init__.py
│     ├── fixtures.py
│     ├── test_login.py
├── utils/
│     ├── __init__.py
│     ├── Constants.py
├── venv/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
````

## Ejecución ✔️
**Nota**: Es necesario crear un archivo de entorno .env dentro de la carpeta raíz, ya que será útil iniciar sesión en la aplicación con sus propias credenciales durante la ejecución de la prueba y evitar errores durante la ejecución. El archivo de entorno debe contener las siguientes variables y valores según sus credenciales:
```
USERNAME=<valores según sus credenciales>
PASSWORD=<valores según sus credenciales>
```
Los siguientes comandos lo ayudarán a ejecutar casos de prueba según lo que necesite probar:
```
    pytest                          # Run all tests
    pytest -m 'smoke'               # Run smoke tests
    pytest -m 'regression'          # Run regression tests
    pytest --alluredir=<path>       # Run all tests and generate files to launch allure report
    allure <path>                   # Run the allure server
    flake8 '<path>'                 # Run flake8 application (Static testing)
```
Pasos para realizar una ejecución exitosa:
1. Clone el repositorio en su máquina local.
2. Abra un terminal y navegue hasta el directorio del proyecto.
3. Ejecute el comando pip install -r requirements.txt para instalar las dependencias necesarias.
4. Inicie Appium Server.
5. Conecte su celular físico mediante USB con la aplicación demo. Enlace de descarga del APK: [Android.SauceLabs.Mobile.Sample.app.2.7.1.apk](https://github.com/saucelabs/sample-app-mobile/releases)  
6. Ejecute el siguiente comando mediante la terminal:

````
pytest -m 'regression' --alluredir='../reports'

````

Ejemplo:
````
PS E:\Users\1044015\PycharmProjects\ProyectoPOMPython> pytest -m 'regression' --alluredir='../reports' 
============================================================================================== test session starts ===============================================================================================
platform win32 -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0                       
rootdir: E:\Users\1044015\PycharmProjects\ProyectoPOMPython                       
plugins: allure-pytest-2.12.0, dotenv-0.5.2, env-0.8.1, html-3.2.0, metadata-2.0.4
collected 8 items / 1 deselected / 7 selected
````

Resultado:

````
tests\test_logins.py .......    
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json0]
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json1]
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json2]
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json3]
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json4]
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json5]
tests/test_logins.py::TestLoginSwagLabs::test_login_swag_regression[data_json6]
============================================================================ 7 passed, 1 deselected, 9 warnings in 129.14s (0:02:09) ============================================================================= 
PS E:\Users\1044015\PycharmProjects\ProyectoPOMPython>

````

7. Para generar el reporte allure ejecuté el siguiente comando, este comando abrirá una ventana en tu navegador con un reporte más detallado de las pruebas.
 
````
allure serve reports
````
Resultado:

![Allure](https://i.imgur.com/tU1PiXk.png)


## Notas 📝

- Se recomienda ejecutar las pruebas en un dispositivo Android real en lugar de un emulador.
- Asegúrese de que la aplicación esté instalada en su dispositivo móvil antes de ejecutar las pruebas.
- Puede agregar más pruebas en el directorio tests siguiendo la estructura POM.
- Puede agregar más casos de prueba en el directorio utils/data.json
- Para la ejecución del proyecto mediante los comandos mencionados en la sección de ejecución deberán modificar la ruta del archivo .json que se encuentra en el directorio tests/fixtures.py: DATA_PATH = "./utils/data.json" 
- Este proyecto utiliza el patrón de diseño Page Object Model (POM) para organizar las pruebas. Puedes encontrar los archivos relacionados con este patrón en el directorio screens.
- Este proyecto utiliza el framework de pruebas Pytest. Puedes encontrar más información sobre este framework en la documentación oficial: https://docs.pytest.org/en/latest/

## Contribución 🤝

¡Contribuye al proyecto! Aquí están algunas maneras en que puedes hacerlo:

- Reportar un problema
- Sugerir una mejora
- Enviar una pull request

## Licencia 📄

Este proyecto está bajo licencia con fines educativos y de aprendizaje.
