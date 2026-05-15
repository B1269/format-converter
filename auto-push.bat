@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo [%date% %time%] 开始检查代码变更...
git add -A
git status --porcelain > nul
if %errorlevel% neq 0 (
    echo 没有代码变更
    exit /b 0
)

echo 发现代码变更，正在提交...
git commit -m "chore: 自动提交 %date%"

echo 正在推送...
git push origin master
git push origin release-v1.2

echo [%date% %time%] 推送完成
