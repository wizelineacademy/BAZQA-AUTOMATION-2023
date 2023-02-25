
# Dialer Automation Test

This project contains the automation test suite of the native app Dialer.




## Running Tests

To run a test suite, run the following command

```bash
  pytest -v -m smoketests
```

Generate an allure report 
```bash
  py.test --alluredir=reports ./tests
  
  allure serve reports
```
