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

:: Start backend with venv Python
echo [2/3] Starting backend (Python)...
cd /d "%~dp0backend"
start "Backend" "%~dp0backend\venv\Scripts\python.exe" main.py

timeout /t 2 /nobreak >nul

:: Start frontend
echo [3/3] Starting frontend (Vite)...
cd /d "%~dp0frontend"
start "Frontend" cmd /c "npm run dev"

echo.
echo ========================================
echo     Services Started!
echo     Backend: http://localhost:8000
echo     Frontend: http://localhost:5173
echo ========================================
echo.
pause
