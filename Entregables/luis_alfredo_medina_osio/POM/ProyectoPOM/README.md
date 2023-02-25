
# Saucedemo Test

This project contains the automation test suite of Login app Saucedemo.


## Running Tests

To run a test suite, run the following command

```PowerShell
  pytest -m smoketest
  pytest -m regresion

```

Generate an allure report 
```PowerShell
  py.test --alluredir=reports ./tests
  
  allure serve reports
```
