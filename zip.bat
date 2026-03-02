@echo off
chcp 65001 >nul
title Skill Packer

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

set "EXECUTABLE=%SCRIPT_DIR%dist\skill-packer.exe"

if not exist "%EXECUTABLE%" (
    echo [ERROR] Executable not found: %EXECUTABLE%
    echo [INFO] Please run build.bat first to build the executable
    pause
    exit /b 1
)

echo [INFO] Starting Skill Packer...
"%EXECUTABLE%"

pause
