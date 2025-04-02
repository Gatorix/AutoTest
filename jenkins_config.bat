:: Close all chrome task
taskkill /F /iM chrome.exe

:: Set the project root directory.
set PYTHONPATH=%WORKSPACE%

:: Set the base environment and virtual environment location.
set benv=C:/Users/kddadmin/AppData/Local/Programs/Python/Python38
set venv=D:/ZWY_AutoTest/venv
set venv_python=%venv%\Scripts\python

:: Set pip and python executable file.
set pip=%venv%/Scripts/pip
set python=%venv%/Scripts/python
set pytest=%venv%/Scripts/pytest
set allure=D:/ZWY_AutoTest/allure-2.20.1/bin/allure

:: Check and create virtual environment.
if not exist %venv% (
    call "%benv%/python" -m venv %venv%
    call "%venv%/Scripts/activate"
    call "%venv_python%" -m pip install --upgrade pip
)

:: Update dependencies.
:: "%pip%" install -r ./requirements.txt -q

:: Execute testcases
if %is_batch% == true (
    call %python% %WORKSPACE%/run_batch.py
    exit 0
) else (
    call %python% %WORKSPACE%/run.py
    exit 0
)

:: hudson.security.csrf.GlobalCrumbIssuerConfiguration.DISABLE_CSRF_PROTECTION=true
