@echo off
chcp 65001 >nul
title 格式转换工具 - 停止服务

echo.
echo ========================================
echo     正在停止所有服务...
echo ========================================
echo.

:: 停止后端 (Python)
echo [1/3] 停止后端服务...
taskkill /F /IM python.exe 2>nul
if %errorlevel% equ 0 (
    echo   ✅ 后端已停止
) else (
    echo   ℹ️  后端未运行
)

:: 停止前端 (Node/Vite)
echo [2/3] 停止前端服务...
for /f "tokens=2" %%a in ('tasklist /FI "WINDOWTITLE eq *vite*" /FO LIST 2^>nul ^| find "PID:"') do taskkill /F /PID %%a 2>nul
for /f "tokens=2" %%a in ('tasklist /FI "WINDOWTITLE eq *npm*" /FO LIST 2^>nul ^| find "PID:"') do taskkill /F /PID %%a 2>nul
echo   ✅ 前端已停止

:: 停止LibreOffice
echo [3/3] 停止LibreOffice...
taskkill /F /IM soffice.exe 2>nul
echo   ✅ LibreOffice已停止

echo.
echo ========================================
echo     所有服务已停止！
echo ========================================
echo.
pause
