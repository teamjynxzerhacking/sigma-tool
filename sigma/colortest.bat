@echo off
:: Povolit ANSI
for /f "delims=" %%A in ('echo prompt $E ^| cmd') do set "ESC=%%A"

:: Červený text
echo %ESC%[31m████████╗ ██████╗ ██████╗ ██╗%ESC%[0m
:: Bílý text
echo %ESC%[37mcool text%ESC%[0m

pause
