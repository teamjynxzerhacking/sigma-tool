@echo off

set "DesktopDir=%USERPROFILE%\Desktop"





:: přejdi do složky sigma i jednotky  
cd /D "%DesktopDir%\sigma\tools"



chcp 65001 >nul
:verify
echo ██╗   ██╗███████╗██████╗ ██╗███████╗██╗   ██╗    ██████╗ ██╗     ███████╗ █████╗ ███████╗███████╗
echo ██║   ██║██╔════╝██╔══██╗██║██╔════╝╚██╗ ██╔╝    ██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔════╝
echo ██║   ██║█████╗  ██████╔╝██║█████╗   ╚████╔╝     ██████╔╝██║     █████╗  ███████║███████╗█████╗  
echo ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝    ╚██╔╝      ██╔═══╝ ██║     ██╔══╝  ██╔══██║╚════██║██╔══╝  
echo  ╚████╔╝ ███████╗██║  ██║██║██║        ██║       ██║     ███████╗███████╗██║  ██║███████║███████╗
echo   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                 
powershell -NoLogo -Command "Write-Host ' do you understand that i am not responsible for the damage caused by this program?' -ForegroundColor Red"
echo y=yes n=no
set /p verify=enter y or n :
if /i "%verify%"=="y" goto main
if /i "%verify%"=="n" goto bye
if "%verify%"=="" (
    echo No Option entered
    pause
     goto verify
)
:bye
echo you are not allowed to use this program
pause
exit
:main
cls
echo ========================================================================================================================================================
echo                        ███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ██╗   ██╗     ██████╗    ██╗
echo                        ████╗ ████║██╔════╝████╗  ██║██║   ██║    ██║   ██║    ██╔═████╗  ███║
echo                        ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ██║   ██║    ██║██╔██║  ╚██║
echo                        ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ╚██╗ ██╔╝    ████╔╝██║   ██║
echo                        ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝     ╚████╔╝     ╚██████╔╝██╗██║
echo                        ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝       ╚═══╝       ╚═════╝ ╚═╝╚═╝
                                                                                                                    
echo =======================================================================================================================================================


powershell -NoLogo -Command "Write-Host -ForegroundColor Red 'f' -NoNewline; Write-Host -ForegroundColor White ' the government'"
echo sigma tool by-team jynxzer
echo (feel free to use this maliciosly)
echo (i am not responsible for any damage caused by this program)
echo ==============================
echo.
echo 1 - ping   (ping ip/url)
echo 2 - search (find a ip of a website)
echo 3 - iplook (ip lookup)
echo 4 - doxmachine (finds peoples instagram facebok titkok, etc)
echo 5 - pictomap (upload a photo and see where its been taken in)
echo 6 - wifimap (find wifis in your city/village etc)
echo 7 - dos (denial of service)
echo 8 - toolkit (external tools)
echo 0 - readme (something about us)
echo.
set /p value=enter command:



if /i "%value%"=="1" goto ping
if /i "%value%"=="ping" goto ping

if /i "%value%"=="2" goto search
if /i "%value%"=="search" goto search

if /i "%value%"=="3" goto iplookup
if /i "%value%"=="iplook" goto iplookup

if /i "%value%"=="dox" goto doxmachineload
if /i "%value%"=="4" goto doxmachineload
if /i "%value%"=="doxmachine" goto doxmachineload
if /i "%value%"=="skiploadox" goto doxmachine
if /i "%value%"=="5" goto pic2map
if /i "%value%"=="pictomap" goto pic2map
if /i "%value%"=="6" goto wifimap
if /i "%value%"=="wifimap" goto wifimap
if /i "%value%"=="7" goto ddosload
if /i "%value%"=="dos" goto ddosload
if /i "%value%"=="8" goto toolkit
if /i "%value%"=="toolkit" goto toolkit
if /i "%value%"=="root" goto root_admin
if /i "%value%"=="0" goto readme
echo ███████╗██████╗ ██████╗  ██████╗ ██████╗         ██╗
echo ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╗██╔╝
echo █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    ╚═╝██║ 
echo ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    ██╗██║ 
echo ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║    ╚═╝╚██╗
echo ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝        ╚═╝
pause
goto main
                                                    
pause
goto main
:readme
start readme.py
pause
goto main
:root_true
cls
echo                         ██████╗  ██████╗  ██████╗ ████████╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
echo                         ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝    ████╗ ████║██╔════╝████╗  ██║██║   ██║
echo                         ██████╔╝██║   ██║██║   ██║   ██║       ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
echo                         ██╔══██╗██║   ██║██║   ██║   ██║       ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
echo                         ██║  ██║╚██████╔╝╚██████╔╝   ██║       ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
echo                         ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
set /p root=Enter option: 
if "%root%"=="1" goto root1
if "%root%"=="home" goto main
if "%root%"=="gui" goto gui
:gui
start gui1.py
pause
goto root_true
echo Invalid option!
pause
goto root_true

:root1
echo You selected root option 1
pause
goto root_true
                                                          
:root_admin
set /p user=Enter user: 
set /p pas=Enter password: 

:: Ověření
if "%user%"=="admin" if "%pas%"=="123" (
    echo login suceful
) else (
    echo wrong user or pas
    goto root_admin
)
pause

goto root_true
:pic2map
start https://www.pic2map.com/
:safety pause
pause
goto main

:wifimap
start https://www.wifimap.io/
:safety pause
pause 
goto main
:toolkit
echo        ████████╗ ██████╗  ██████╗ ██╗         ██╗  ██╗██╗████████╗
echo        ╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║ ██╔╝██║╚══██╔══╝
echo           ██║   ██║   ██║██║   ██║██║         █████╔╝ ██║   ██║   
echo           ██║   ██║   ██║██║   ██║██║         ██╔═██╗ ██║   ██║   
echo           ██║   ╚██████╔╝╚██████╔╝███████╗    ██║  ██╗██║   ██║   
echo           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝   ╚═╝   
echo ==========================tools===============================
echo 1 iplookup [external ip lookup withnout opening chrome]
echo 2 vpn check [checks if your device is connected to a vpn]
set /p tooloption= enter a tool name:
if "%tooloption%"=="1" goto iplookuptool
if "%tooloption%"=="iplookup" goto iplookuptool
if "%tooloption%"=="vpn check" goto vpn_check
if "%tooloption%"=="home" goto main
if "%tooloption%"=="" (
    echo No Option entered

echo ███████╗██████╗ ██████╗  ██████╗ ██████╗         ██╗
echo ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╗██╔╝
echo █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    ╚═╝██║ 
echo ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    ██╗██║ 
echo ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║    ╚═╝╚██╗
echo ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝        ╚═╝
    pause
     goto toolkit
)

echo ███████╗██████╗ ██████╗  ██████╗ ██████╗         ██╗
echo ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╗██╔╝
echo █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    ╚═╝██║ 
echo ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    ██╗██║ 
echo ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║    ╚═╝╚██╗
echo ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝        ╚═╝
pause
goto toolkit

:vpn_check 
start vpndetector.py
pause
goto toolkit
:iplookuptool
pause
start iplookup.py
goto main
                                                           
:ddosload
echo ██████╗ ██████╗  ██████╗ ███████╗
echo ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
echo ██║  ██║██║  ██║██║   ██║███████╗
echo ██║  ██║██║  ██║██║   ██║╚════██║
echo ██████╔╝██████╔╝╚██████╔╝███████║
echo ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
set /p load= enter load method a or b :
if /i "%load%"=="a" goto a
if /i "%load%"=="b" goto b
pause
:a
start ddos.py
pause
goto main
:b
echo ███████╗██████╗ ██████╗  ██████╗ ██████╗         ██╗
echo ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╗██╔╝
echo █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    ╚═╝██║ 
echo ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    ██╗██║ 
echo ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║    ╚═╝╚██╗
echo ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝        ╚═╝
pause
goto main
                                 
:doxmachine
echo ██████╗  ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
echo ██╔══██╗██╔═══██╗╚██╗██╔╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
echo ██║  ██║██║   ██║ ╚███╔╝     ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
echo ██║  ██║██║   ██║ ██╔██╗     ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
echo ██████╔╝╚██████╔╝██╔╝ ██╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
echo ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
set /p info=ENTER FULL Name (example: petr parker)  : 
if "%info%"=="home" goto main
if "%info%"=="" (
    echo No Info entered.
    pause
    goto main
)                                                                                
start https://cs-cz.facebook.com/public/%info%
start https://www.instagram.com/%info%/
start https://www.spokeo.com/%info%
goto main

:doxmachineload
echo                    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
echo                    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
echo                    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗
echo                    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
echo                    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
echo                    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                       
setlocal enabledelayedexpansion
set "bar="

for /l %%i in (1,1,100) do (
    cls
    set "bar=!bar!#"
    echo Loading %%i%%...
    echo [!bar!]
    powershell -command "Start-Sleep -Milliseconds 40"
)
echo loaded
pause
goto doxmachine

:: ========== IP LOOKUP ==========
:iplookup
cls
echo ██╗██████╗ ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗  
echo ██║██╔══██╗██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗ 
echo ██║██████╔╝██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝ 
echo ██║██╔═══╝ ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝  
echo ██║██║     ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║      
echo ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝      
echo.
set /p ip=IP: 
if "%ip%"=="home" goto main
if "%ip%"=="" (
    echo No IP entered.
    pause
    goto main
)

start https://www.g-force.ca/en/hosting/ip-whois?ip=%ip%
start https://whatismyipaddress.com/ip/%ip%
start https://dnschecker.org/reverse-dns.php?query=%ip%
start https://viewdns.info/reverseip/?host=%ip%&t=1

goto main


:: ========== DOMAIN SEARCH ==========
:search
cls
echo ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
echo ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
echo ███████╗█████╗  ███████║██████╔╝██║     ███████║
echo ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
echo ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
echo ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
echo.
echo Enter website (example: google.com)
set /p website=Website: 
if "%website%"=="home" goto main
if "%website%"=="" (
    echo No website entered.
    pause
    goto main
)

start https://www.nslookup.io/domains/%website%/webservers/
start https://dnschecker.org/domain-ip-lookup.php?query=%website%&dns=google
start https://www.nslookup.io/domains/%website%/dns-records/
start https://viewdns.info/reverseip/?host=%website%&t=1

goto main


:: ========== PING ==========
:ping
cls
echo ██████╗ ██╗███╗   ██╗ ██████╗ 
echo ██╔══██╗██║████╗  ██║██╔════╝ 
echo ██████╔╝██║██╔██╗ ██║██║  ███╗
echo ██╔═══╝ ██║██║╚██╗██║██║   ██║
echo ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ 
echo.

set /p target=Enter IP/URL: 
if "%target%"=="home" goto main
if "%target%"=="" (
    echo No target entered.
    pause
    goto main
)

ping "%target%"
pause
goto main