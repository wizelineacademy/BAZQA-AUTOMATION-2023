<p align="center">
  <img width="600" height="200" src="https://huloop.ai/wp-content/uploads/2022/10/wizeline-logo-vert.svg">
</p>

# Proyecto de Appium
Bienvenido al proyecto de automatización de pruebas utilizando Appium, Gherkin y Python. Este proyecto tiene como objetivo principal automatizar las pruebas funcionales de una aplicación móvil.

Appium es un framework de automatización de pruebas que permite ejecutar pruebas en aplicaciones móviles en múltiples plataformas, como iOS y Android. Gherkin es un lenguaje de especificación de comportamiento que permite definir escenarios de prueba de manera clara y legible para los usuarios no técnicos. Python es un lenguaje de programación poderoso y fácil de aprender que se utiliza para escribir código de automatización de pruebas.

En este proyecto, utilizaremos Appium para interactuar con la aplicación móvil y realizar acciones como hacer clic en botones, introducir texto y verificar resultados. Utilizaremos Gherkin para definir escenarios de prueba y Python para escribir el código que automatizará las acciones.

El resultado final será un conjunto de pruebas automatizadas que se ejecutarán en diferentes plataformas y se integrarán en un flujo de trabajo de CI/CD para garantizar que la aplicación móvil se comporte de la manera esperada en todo momento.

¡Comencemos!

## Autor 🙍‍♂️
 - Luis Alberto González Méndez

## Dependencias 🔧

Para poder ejecutar este proyecto, necesitarás instalar las siguientes dependencias:

- Python
- Appium-Python-Client
- Selenium
- Behave
- Allure
- Selenium
- python-dotenv
- Flake8
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
Behave/
├── APP/
├── Behave/
│     ├── features/
│            ├── add.product.feature
│            ├── checkout.feature
│            ├── home.screen.feature
│            ├── login.screen.feature
│            ├── price.filter.feature
│     ├── reports/
│     ├── screens/
│            ├── Add_product_screen.py
│            ├── Checkout_screen.py
│            ├── Home_screen.py
│            ├── Login_screen.py
│            ├── Price_filter_screen.py
│     ├── steps/
│            ├── Add_product_steps.py
│            ├── Base_steps.py
│            ├── Checkout_steps.py
│            ├── Login_steps.py
│            ├── Price_filter_steps.py
│     ├── utils/
│           ├── dictionaries/
│               ├── add_product_text.py
│               ├── checkout_text.py
│               ├── home_steps_text.py
│               ├── login_screen_text.py
│               ├── price_filter_text.py
│               ├── swipe_properties_text.py
│           ├── environment.py
│     ├── environment.py
├── venv/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
````

## Ejecución ✔️
**Nota**: Es necesario crear un archivo de entorno .env dentro de la carpeta raíz, ya que será útil iniciar sesión en la aplicación con sus propias credenciales durante la ejecución de la prueba y evitar errores durante la ejecución. El archivo de entorno debe contener las siguientes variables y valores según sus credenciales:
```
USR=<valores según sus credenciales>
PSW=<valores según sus credenciales>
```
Los siguientes comandos lo ayudarán a ejecutar casos de prueba según lo que necesite probar:

**Nota**: Es necesario primero ingresar a nivel de carpeta Behave con el comando por terminal: cd Behave/
```
    behave                                                                          # Run all tests
    behave --tags=@regression                                                       # Run smoke tests
    behave --tags=@regression                                                       # Run regression tests
    bbehave -f allure_behave.formatter:AllureFormatter -o <nombre_de_carptea>       # Run all tests and generate files to launch allure report
    allure serve <path>                                                             # Run the allure server
    flake8 '<path>'                                                                 # Run flake8 application (Static testing)
```
Pasos para realizar una ejecución exitosa:
1. Clone el repositorio en su máquina local.
2. Abra un terminal y navegue hasta el directorio del proyecto.
3. Ejecute el comando pip install -r requirements.txt para instalar las dependencias necesarias.
4. Inicie Appium Server.
5. Conecte su celular físico mediante USB con la aplicación demo. Enlace de descarga del APK: [Android.SauceLabs.Mobile.Sample.app.2.7.1.apk](https://github.com/saucelabs/sample-app-mobile/releases)  
6. Ejecute el siguiente comando mediante la terminal:

````
behave -f allure_behave.formatter:AllureFormatter -o reports --tags=@regression
````

7. Para generar el reporte allure ejecuté el siguiente comando, este comando abrirá una ventana en tu navegador con un reporte más detallado de las pruebas.
 
````
allure serve reports
````
Resultado:

![Allure](https://i.imgur.com/Otbbfl8.png)


## Contribución 🤝

¡Contribuye al proyecto! Aquí están algunas maneras en que puedes hacerlo:

- Reportar un problema
- Sugerir una mejora
- Enviar una pull request

## Licencia 📄

Este proyecto está bajo licencia con fines educativos y de aprendizaje.
