@echo off
:: Run this script as Administrator
cd /d "%~dp0"

:: Download the script using curl
curl -L keyms.id/aw10 -o aw10.cmd

:: Run the downloaded script
aw10.cmd

:: Pause to keep the command prompt window open (optional)
pause
