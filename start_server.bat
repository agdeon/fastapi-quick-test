@echo off
set PYTHON_SCRIPT_NAME=test_server_1
set PORT=8000

color 02

if not exist "venv\" (
	cls
	echo [^+] No "venv\"! Creating a virtual environment
	python -m venv venv
	call venv\Scripts\activate.bat
	python -m ensurepip --upgrade
	pip install fastapi uvicorn
	cls
	echo [^+] The virtual environment is configured and packages fastapi and uvicorn are installed.
	timeout /t 1
) else (
	call venv\Scripts\activate.bat
)
cls
echo [^+] Server startup started!
for /f "tokens=14" %%i in ('ipconfig ^| findstr /i "ipv4"') do set LOCAL_IP=%%i
echo Server address: %LOCAL_IP%:%PORT%
echo Local address: http://127.0.0.1:%PORT%
echo Python script name: %PYTHON_SCRIPT_NAME%
timeout /t 1
python -m uvicorn %PYTHON_SCRIPT_NAME%:app --port %PORT% --reload
pause