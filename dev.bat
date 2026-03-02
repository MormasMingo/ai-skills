@echo off
chcp 65001 >nul
title Skill Packer - Dev Mode

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

echo [INFO] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [INFO] Checking dependencies...
python -c "import colorama" >nul 2>&1
set "COLORAMA_MISSING=%errorlevel%"
python -c "import keyboard" >nul 2>&1
set "KEYBOARD_MISSING=%errorlevel%"

if "%COLORAMA_MISSING%"=="1" (
    echo [INFO] Installing colorama...
    pip install colorama
)

if "%KEYBOARD_MISSING%"=="1" (
    echo [INFO] Installing keyboard...
    pip install keyboard
)

echo [INFO] Starting Skill Packer in dev mode...
python main.py

pause
