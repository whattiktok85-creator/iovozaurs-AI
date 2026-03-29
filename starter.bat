@echo off
title iovozaur-AI Launcher
color 0b

echo [iovozaur-AI] Checking environment...

py -3.12 -c "import aiogram" 2>nul
if %errorlevel% neq 0 (
    echo [SYSTEM] aiogram not found. Installing...
    py -3.12 -m pip install aiogram --quiet
)

py -3.12 -c "import groq" 2>nul
if %errorlevel% neq 0 (
    echo [SYSTEM] groq not found. Installing...
    py -3.12 -m pip install groq --quiet
)

echo [iovozaur-AI] Libraries are ready!
echo [iovozaur-AI] Launching script...
echo -------------------------------------

cscript //nologo information.vbs
py -3.12 "iovozaurs-ai.py"

if %errorlevel% neq 0 (
    echo [ERROR] Launch failed. Check if Python 3.12 is installed.
    pause
)
pause
