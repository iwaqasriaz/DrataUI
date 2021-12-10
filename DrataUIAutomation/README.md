# Drata

### Pre-requisite:
Create a separate env for running this project.
activate the env in the terminal then 
run :<br>```pip install -r requirements.txt```<br>
make sure you have setup for java and allure in your system.

### Run test
```
behave -f allure_behave.formatter:AllureFormatter -o reports
```
# view Reports
1.``` allure serve reports```