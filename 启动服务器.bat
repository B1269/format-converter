@echo off
title Format Converter - Start

cd /d "%~dp0"

echo.
echo ========================================
echo     Format Converter - Starting Services
echo ========================================
echo.

echo [1/3] Stopping existing services...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM soffice.exe >nul 2>&1
timeout /t 1 /nobreak >nul

cd /d "%~dp0frontend"
echo [2/3] Starting backend and frontend...
echo.

npm run start:win
