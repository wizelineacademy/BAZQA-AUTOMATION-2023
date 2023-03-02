
# Automatizacion_POM

This project contains the automation test suite of the native app Dialer.

# Running Tests
To run a test suite, run the following command
```bash
   pytest -v -m Regresion
   pytest -v -m SmokeTest
   
```
Generate an allure report 
```bash
py.test --alluredir=Reportes
  
allure serve Reportes
```