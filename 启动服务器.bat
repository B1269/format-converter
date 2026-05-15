@echo off
title Format Converter - Start

cd /d "%~dp0"

echo.
echo ========================================
echo     Format Converter - Starting Services
echo ========================================
echo.

:: Stop existing services
echo [1/4] Stopping existing services...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM soffice.exe >nul 2>&1
timeout /t 1 /nobreak >nul

:: Start backend with venv Python
echo [2/4] Starting backend (Python)...
cd /d "%~dp0backend"
start "Backend" "%~dp0backend\venv\Scripts\python.exe" main.py

timeout /t 2 /nobreak >nul

:: Start frontend
echo [3/4] Starting frontend (Vite)...
cd /d "%~dp0frontend"
start "Frontend" cmd /c "npm run dev"

echo.
echo ========================================
echo     All Services Started!
echo     Backend: http://localhost:8000
echo     Frontend: http://localhost:5173
echo ========================================
echo.
echo Press any key to close this window...
pause >nul
