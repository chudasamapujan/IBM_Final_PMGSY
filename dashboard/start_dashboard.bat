@echo off
title Infrastructure Prediction Dashboard

echo.
echo ===============================================
echo  Infrastructure Prediction Dashboard
echo  AI-Powered Infrastructure Project Forecasting
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo 📥 Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
if not exist "venv\Scripts\flask.exe" (
    echo 📥 Installing dependencies...
    pip install -r requirements.txt
)

REM Start the dashboard
echo 🚀 Starting dashboard...
python start_dashboard.py

echo.
echo 👋 Dashboard stopped. Press any key to exit...
pause >nul
