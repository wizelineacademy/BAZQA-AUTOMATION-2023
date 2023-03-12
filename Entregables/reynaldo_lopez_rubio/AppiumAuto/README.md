# AppiumAuto

1. Introducción
Este marco de automatización se creó para ejecutar casos de prueba automatizados con fines educativos. 
Solo necesita descargar el proyecto, instalar las dependencias y ejecutarlo.
Este framework fue construido siguiendo el patrón de diseño de Page Object Model y utiliza BDD (Gherkin)
como lenguaje para una mejor comprensión de los casos de prueba.
Requisitos que necesitas en tu computadora:
* Derechos de administrador en su computadora para descargar e instalar aplicaciones
* pyCharm Community Edition.
* Emulador de Andrid Studio.
* Appium Server
* Appium Inspector


2. Herramientas
Las herramientas y el lenguaje de programación utilizados en este proyecto son:
* Python como lenguaje de programación
* Git como software de versión de control
* Github alojar el código de la aplicacion
* Flake8 como herramientas para comprobar su código base contra el estilo de codificación (PEP8)
* Allure Reports como herramienta de generacion de Reporte


3 installation
3.1 Ejecutando el framework
1. Para comenzar, primero clone el repositorio
2. Abra una terminal o línea de comando
3. Instalar requirement.md (pip install -r requirements.txt)
4. Crear archivo .env con los registros STANDARD_USER='' y PASSWORD=''
5. Ejecute las pruebas (Para ejecutar los cp de regresion y e2e, Abajo
se describe los pasos para la configuracion)
6. Espere a que finalice la ejecución de la prueba.
7. Genere el reporte de pruebas con allure report


# Running Tests
Para correr las pruebas e2e y de regresion
realizar la siguiente configuracion 
1. Seleccionar select run - Edit configurations
2. Añadir una nueva configuracion 
3. Cambiar script path por Module name y buscar behave
4. Agrear los siguientes parametros para los cp de regresion, en caso de e2e solo cambiar
etiqueta de regresion por e2e
--tags=regresion 
-k
-D
platform=android
-D
platform_version=8.1
-D
testing_process=serial
-D
driver_location=local
-D
device_name=Prueba
-f
pretty
features/
5. En working directory agregar la ruta de la carperta Behave
6. Pulsar apply y OK

Para Generar el reporte en allure
1. Intale allure report(pip install allure-behave)
2. Ejecute la validacion
behave -f allure_behave.formatter:AllureFormatter -o reports/ Behave
3. Genere el Reporte
allure serve reports


Para Ejecucion de flake8 (Analisis de Codigo)

1. instale flake8
python -m pip install flake8
2.Se tiene que correr el scrip para ignorar el F811
flake8 --ignore=F811 E:\Users\1059769\Documents\GitHub\BAZQA-AUTOMATION-2023\Entregables\reynaldo_lopez_rubio\AppiumAuto\Behave