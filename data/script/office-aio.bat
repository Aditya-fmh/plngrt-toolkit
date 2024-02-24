@echo off
:: Run this script as Administrator
cd /d "%~dp0"

:: Download the script using curl
curl -L keyms.id/aso -o aso.cmd

:: Run the downloaded script
aso.cmd

:: Pause to keep the command prompt window open (optional)
pause
