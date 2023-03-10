# AppiumAuto

This project contains the automation test suite of the native app Dialer.
Pre-requisitos 📋
behave==1.2.6
Appium-Python-Client==1.0.2
python-dotenv~=0.19.2
selenium==3.141.0

Intalacion

pip install -r requirements.txt



# Running Tests
To run a test suite, run the following command
```bash
   pytest -v -m Regresion
   pytest -v -m SmokeTest
   
```
Generate an allure report
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ Behave

allure serve reports
```