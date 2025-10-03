@echo off
setlocal

REM Get the virtual environment name (modify if needed)
set VENV_NAME=my_venv

REM Check if the virtual environment directory exists
if exist "%VENV_NAME%" (
    REM Virtual environment exists
    echo Virtual environment '%VENV_NAME%' exists.
) else (
    echo Virtual environment '%VENV_NAME%' does not exist so creating...
    python -m venv %VENV_NAME%
    echo Virtual environment has been created
)

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate.bat
echo Checking and installing required libraries
python -m pip install -r requirements.txt

REM Call your Python script with necessary arguments
python doc_enc_dec.py %*

REM Deactivate virtual environment
call deactivate

endlocal
