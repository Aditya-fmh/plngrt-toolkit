@echo off
title Aktivasi Windows 10 Tanpa Software!&cls&(net session >nul 2>&1)
if %errorLevel% GTR 0 (echo.&echo Aktivasi tidak bisa dilanjut, Anda harus Run CMD as administrator...&echo.&goto halt)
echo =====================================================================================&echo #Project: Aktivasi Windows 10 Tanpa Software&echo =====================================================================================&echo.&echo #Supported products:&echo - Windows 10 Home&echo - Windows 10 Home N&echo - Windows 10 Home Single Language&echo - Windows 10 Home Country Specific&echo - Windows 10 Professional&echo - Windows 10 Professional N&echo - Windows 10 Education&echo - Windows 10 Education N&echo - Windows 10 Enterprise&echo - Windows 10 Enterprise N&echo - Windows 10 Enterprise LTSB&echo - Windows 10 Enterprise LTSB N&echo.&echo.&echo =====================================================================================&echo Mengaktivasi Windows 10 anda, silahkan tunggu...&echo =====================================================================================&(cscript //nologo slmgr.vbs /ckms >nul || goto wshdisabled)&cscript //nologo slmgr.vbs /upk >nul&cscript //nologo slmgr.vbs /cpky >nul&set i=1&wmic os | findstr /I "enterprise" >nul
if %errorlevel% EQU 0 (cscript //nologo slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43 >nul&cscript //nologo slmgr.vbs /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 >nul&cscript //nologo slmgr.vbs /ipk WNMTR-4C88C-JK8YV-HQ7T2-76DF9 >nul&cscript //nologo slmgr.vbs /ipk 2F77B-TNFGY-69QQF-B8YKP-D69TJ >nul&cscript //nologo slmgr.vbs /ipk DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ >nul&cscript //nologo slmgr.vbs /ipk QFFDN-GRT3P-VKWWX-X7T3R-8B639 >nul&goto server) else wmic os | findstr /I "home" >nul
if %errorlevel% EQU 0 (cscript //nologo slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 >nul&cscript //nologo slmgr.vbs /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM >nul&cscript //nologo slmgr.vbs /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH >nul&cscript //nologo slmgr.vbs /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR >nul&goto server) else wmic os | findstr /I "education" >nul
if %errorlevel% EQU 0 (cscript //nologo slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 >nul&cscript //nologo slmgr.vbs /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ >nul&goto server) else wmic os | findstr /I "10 pro" >nul
if %errorlevel% EQU 0 (cscript //nologo slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX >nul&cscript //nologo slmgr.vbs /ipk MH37W-N47XK-V7XM9-C7227-GCQG9 >nul&goto server) else (goto notsupported)
:server
if %i% GTR 5 (goto busy) else if %i% LEQ 3 (set KMS=s1.keyms.id) else if %i% LEQ 5 (set KMS=e8.us.to)
cscript //nologo slmgr.vbs /skms %KMS%:1688 >nul
:ato
echo.&cscript //nologo slmgr.vbs /ato | find /i "successfully" > temp.txt && (echo.&echo Silahkan donasi via saweria.co/bagitecno untuk menyelesaikan aktivasi Windows 10 anda.&echo.& if errorlevel 2 exit) || (echo Sepertinya butuh waktu lebih, silahkan tunggu... & echo. & echo. & set /a i+=1 & timeout /t 10 >nul & goto server)&timeout /t 7 >nul&explorer "https://saweria.co/bagitecno"&echo.
set /P csawer=Apakah anda sudah donasi? (ketik YES jika sudah lalu Enter) : &echo.
if /i "%csawer%"=="YES" (echo.&echo =====================================================================================&echo.&type temp.txt&echo.&echo =====================================================================================&echo.&echo.&goto halt) else if "%csawer%"=="" (goto halt) else (goto halt)
:notsupported
echo =====================================================================================&echo.&echo Maaf, Windows 10 anda tidak support.&echo.&goto halt
:wshdisabled
echo =====================================================================================&echo.&echo Maaf, aktivasi gagal karena Windows Script Host access is disabled.&echo.&echo Solusinya, ikuti panduan pada video tutorial yang terbuka untuk mengizinkan Windows Script.&echo.&timeout /t 7 >nul&explorer "https://youtu.be/vqGMSQnWMIY"&goto halt
:busy
echo =====================================================================================&echo.&echo.&echo Maaf, aktivasi gagal karena koneksi internet anda tidak stabil.&echo.&echo Silahkan sambungkan Laptop anda ke WiFi lain kemudian ulangi lagi cara ini.&echo.&goto halt
:halt
cd %~dp0&del %0 >nul&pause >nul