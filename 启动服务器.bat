@echo off
title Format Converter

cd /d "%~dp0"

echo.
echo ========================================
echo     Format Converter - Starting
echo ========================================
echo.

:: Stop existing services
echo [1/3] Stopping services...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM soffice.exe >nul 2>&1
timeout /t 1 /nobreak >nul

:: Start services
echo [2/3] Starting backend and frontend...
cd /d "%~dp0frontend"
npm run start:win
