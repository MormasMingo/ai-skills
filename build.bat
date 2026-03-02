@echo off
chcp 65001 >nul
title Build Skill Packer

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

echo [INFO] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [INFO] Installing build dependencies...
pip install pyinstaller

echo [INFO] Building executable...
pyinstaller --onefile --name skill-packer --console main.py

echo [INFO] Build complete!
echo [INFO] Executable location: dist\skill-packer.exe
pause
