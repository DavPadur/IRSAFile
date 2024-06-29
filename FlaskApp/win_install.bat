@echo off
SETLOCAL EnableDelayedExpansion

:: Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Installing Python...
    powershell -Command "Start-Process msiexec.exe -ArgumentList '/i https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1' -NoNewWindow -Wait"
) ELSE (
    echo Python is already installed.
)

:: Upgrade pip
python -m pip install --upgrade pip

:: Install dependencies
python -m pip install --no-input flask selenium pyvo

echo Installation complete.
pause
