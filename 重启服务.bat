@echo off
chcp 65001 >nul
title 格式转换工具 - 重启服务

echo.
echo ========================================
echo     格式转换工具 - 重启服务
echo ========================================
echo.

:: 进入项目根目录
cd /d "%~dp0"

:: 停止现有服务
echo [1/3] 停止现有服务...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM soffice.exe >nul 2>&1
timeout /t 2 /nobreak >nul

:: 同时启动后端和前端（在同一窗口）
echo [2/3] 启动服务...
echo.
echo ═══════════════════════════════════════
echo   后端: http://localhost:8000
echo   前端: http://localhost:5173
echo ═══════════════════════════════════════
echo.

:: 启动后端和前端（并行）
start /B cmd /c "cd /d %~dp0backend && python main.py"
start /B cmd /c "cd /d %~dp0frontend && npm run dev"

:: 等待服务就绪
timeout /t 8 /nobreak >nul

:: 打开浏览器
echo [3/3] 打开浏览器...
start http://localhost:5173

echo.
echo ========================================
echo     重启完成！
echo ========================================
echo.
echo   两个服务已在后台运行
echo   关闭窗口即可停止所有服务
echo.
pause
