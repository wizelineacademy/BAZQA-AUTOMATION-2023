# Automatización Appium + Behave
Este repositorio contiene un ejemplo de proyecto de automatización utilizando behave.
## Estructura del proyecto 
```` 
├── AppiumAuto
    ├── Behave
        ├── App
            ├── saucedemo.apk
        ├── features
            ├── cart.feature
            ├── checkout.feature
            ├── home.screen.feature
            ├── log.in.feature
            ├── navbar.feature
            ├── product.feature
        ├── screens
            ├── cart
                ├── cart_screen.py
            ├── checkout
                ├── checkout_complete_screen.py
                ├── checkout_payment_screen.py
                ├── checkout_review_screen.py
                ├── checkout_screen.py
            ├── navbar
                ├── sort_screen.py
            ├── products
                ├── product_screen.py
            ├── side_menu
                ├── log_in_screen.py
                ├── side_menu_screen.py
            ├── home_screen.py
        ├── steps
            ├── cart
                ├── cart-steps.py
            ├── checkout
                ├── checkout_complete_steps.py
                ├── checkout_payment_steps.py
                ├── checkout_review_steps.py
                ├── checkout_steps.py
            ├── navbar
                ├── sort_by_steps.py
            ├── products
                ├── product_steps.py
            ├── side_menu
                ├── log_in_steps.py
                ├── side_menu_steps.py
            ├── base_steps.py
            ├── home_steps.py
        ├── utils
        ├── .env
        ├── enviroment.py
        ├── requirements.txt
        ├── README.md
    ├── venv
        
```` 
## Requerimientos previos
Se requiere tener instalado:
- Android Studio 
- IDE: PyCharm
- Appium server
- Appium inspector

## Configuración del proyecto
Desde PyCharm ir a las preferencias del proyecto, ahí elegir como python interpreter una versión de python 3 o superior, así como las librerías que se encuentran a continuación, las cuales se deberan agregar en el `requirements.txt`
````
behave==1.2.6
Appium-Python-Client==2.8.1
python-dotenv==1.0.0
selenium==4.8.2
````
Para instalar lo indicado en el archivo requirements, será necesario ejecutar en consola el siguiente comando:
`pip3 install -r requirements.txt`
##APK
El apk utilizado para la creación de los casos de prueba se localiza en la carpeta `App`.
##Capabilities 
Para  este proyecto se utilizo un emulador Pixel XL con android 11, en caso de requerir cambiar las capabilities estás se tendrán que editar en el `environment.py`  del proyecto:
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
## Datos de prueba
En el archivo `.env` se deberán agregar los datos de los usuarios necesarios para las pruebas, completando la siguiente información:
```bash
STANDARD_USER =
PASSWORD = 
FULL_NAME = 
ADDRESS = 
CITY = 
ZIP_CODE = 
COUNTRY = 
CARD = 
EXP_DATE = 
SEC_CODE = 
```
## Ejecución de tests
#### Ejecutar pruebas de regresión
Crear una configuración para correr desde pycharm agregando los siguientes parametros:
```
/dirección donde se encuentra ubicado el proyecto hasta la carpeta behave
--tags=regression
-k
-D
platform=android
-D
platform_version=11
-D
device_name=PixelXL
```
Se debera de cambiar script path por module name y seleccionar behave, para el working directory se debera de agregar la ruta hasta la carpeta behave.
La configuración tendra que mostrarse como la siguiente imagen:
![](../../regresion.png)
#### Ejecutar pruebas de humo
Crear una configuración para correr desde pycharm agregando los siguientes parametros:
```
/dirección donde se encuentra ubicado el proyecto hasta la carpeta behave
--tags=smoke
-k
-D
platform=android
-D
platform_version=11
-D
device_name=PixelXL
```
Se debera de cambiar script path por module name y seleccionar behave, para el working directory se debera de agregar la ruta hasta la carpeta behave.
La configuración tendra que mostrarse como la siguiente imagen:
![](../../smoke.png)


##Generar reporte con allure
Generación de reportes:
Se debe instalar allure-behave con el siguiente comando:
```pip3 install allure-behave```

Para ejecutar con el tag smoke:
```bash
  behave -f  allure_behave.formatter:AllureFormatter -o reports --tags=@smoke

  allure serve reports
```
Para ejecutar con el tag regression:
```bash

  behave -f  allure_behave.formatter:AllureFormatter -o reports --tags=@regresion

  allure serve reports
```
*Nota: al ejecutar al generar el reporte, si se requiere generar uno distinto requiere de eliminar todos los archivos de la carpeta reportes*

## Análisis de código estático 
Instalar flake8 con el comando `pip3 install flake8`
Se utiliza la herramienta flake8 para el análisis de código estático:
```bash
 flake8 ./carpeta_a_analizar
```
En el caso de proyecto se validaron:
```bash
 flake8 ./features
```
```bash
 flake8 ./screens
```


