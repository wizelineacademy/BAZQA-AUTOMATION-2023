# Automatización POM Saucedemo con Appium + Pytest
Este repositorio contiene una estructura POM con la cual se automatizaron las pruebas del flujo de login en la aplicación Saucedemo, 
utilizando las siguientes herramientas:
- Pytest
- Allure 
- Flake8 
## Estructura del proyecto 
```` 
├── Saucedemo_Automation_AKGV
    ├── App
        ├── saucedemo.apk
    ├── reportes
    ├── screens
        ├── baseScreen.py
        ├── screenLogin.py
        ├── screenMenu.py
        ├── screenProduct.py
    ├── tests
        ├── conftest.py
        ├── test_iniciosesion.py
    ├── utils
        ├── actionsLibrary.py
    ├── venv
    ├── pytest.ini
    ├── README.md
```` 
## Requerimientos previos
Se requiere tener instalado:
- Android Studio 
- IDE: PyCharm
- Appium server
- Appium inspector

## Configuración del proyecto
Desde PyCharm ir a las preferencias del proyecto, ahí elegir como python interpreter una versión de python 3 o superior, adicional instalar las siguientes librerías:
- Test Runner: Pytest
- Appium-Python-Client
- allure-pytest
- allure-python-commons
- flake8

##APK
El apk utilizado para la creación de los casos de prueba se localiza en la carpeta `App`.
##Capabilities 
Para  este proyecto se utilizo un emulador Pixel XL con android 11, en caso de requerir cambiar las capabilities estás se tendrán que editar en el `conftest.py`  del proyecto:
```bash
{
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "PixelXL",
    "appium:automationName": "UiAutomator2",
    "appium:app":
        "ruta donde se encuentra el apk"
}
```
*Nota: se debera editar la ruta donde se encuentra ubicada la app*
## Usuarios de prueba
En el archivo `pytest.ini` se deberán agregar los datos de los usuarios necesarios para las pruebas, completando la siguiente información:
```bash
{
    USERNAMESUCCESS=
    PASSWORDSUCCESS=
    USERNAMENONEXISTENT=
    NODATA=
    USERNAMEWITHEMOJI=
}
```
## Ejecución de tests 
#### Ejecutar todos los tests de inicio de sesión
```bash
 pytest 
```
#### Ejecutar pruebas de regresión
- Ejecución vía Terminal
```bash
  pytest -m regression
```
- Ejecución mediante Run configuration 
![image](https://user-images.githubusercontent.com/28547374/221060922-552a406f-5dbc-4069-a845-cbafa95bbe03.png)

#### Ejecutar pruebas de humo
- Ejecución vía Terminal
```bash
  pytest -m smoke
```
- Ejecución mediante Run configuration 
![image](https://user-images.githubusercontent.com/28547374/221060873-59902e9e-cad2-492e-b047-58bdde542a0d.png)

##Generar reporte con allure
Generación de reportes:
```bash
  pytest --alluredir=reportes ./tests
  
  allure serve reportes
```
Generación de reportes por mark de la prueba

```bash
 pytest -m smoke  --alluredir=reportes ./tests
 allure serve reportes
```
*Nota: al ejecutar al generar el reporte, si se requiere generar uno distinto requiere de eliminar todos los archivos de la carpeta reportes*
## Análisis de código estático 

Se utiliza la herramienta flake8 para el análisis de código estático:
```bash
 flake8 ./carpeta_a_analizar
```
En el caso de proyecto se validaron:
```bash
 flake8 ./screens
```
```bash
 flake8 ./tests
```
```bash
 flake8 ./utils
```

