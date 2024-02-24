@echo off
:: Run this script as Administrator
cd /d "%~dp0"

:: Register necessary DLL files for Windows Script Host
regsvr32 %systemroot%\system32\vbscript.dll /s
regsvr32 %systemroot%\system32\jscript.dll /s

:: Display a message indicating success or failure
if %errorlevel% equ 0 (
    echo Windows Script Host has been enabled successfully.
) else (
    echo Failed to enable Windows Script Host.
)

:: Pause to keep the command prompt window open (optional)
pause
