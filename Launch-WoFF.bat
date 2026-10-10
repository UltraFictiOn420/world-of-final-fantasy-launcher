@echo off
setlocal EnableExtensions DisableDelayedExpansion
rem World of Final Fantasy Standard-User Launcher v1.0.0
rem Copyright (c) 2026 UltraFictiOn420. MIT License; see LICENSE.
rem Read this file in Notepad before running it. Nothing here downloads code.
rem Put beside WOFF.exe, or pass the game folder in quotes as the first argument.
set "woffGameDir=%~dp0"
if not "%~1"=="" set "woffGameDir=%~1"
if not exist "%woffGameDir%\WOFF.exe" goto missingGame
if not exist "%woffGameDir%\resource\" goto missingResources
if not exist "%woffGameDir%\steam_appid.txt" goto missingAppId

rem Read-only checks: caller privileges, an existing game instance, and Steam.
rem RunAsInvoker inherits privileges; it cannot lower an elevated caller's token.
powershell.exe -NoLogo -NoProfile -NonInteractive -Command "$woffIdentity=[Security.Principal.WindowsIdentity]::GetCurrent(); $woffPrincipal=New-Object Security.Principal.WindowsPrincipal($woffIdentity); if($woffPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)){exit 10}; if(Get-Process -Name WOFF -ErrorAction SilentlyContinue){exit 11}; if(-not (Get-Process -Name steam -ErrorAction SilentlyContinue)){exit 12}; exit 0"
if errorlevel 13 goto failedCheck
if errorlevel 12 goto missingSteam
if errorlevel 11 goto alreadyRunning
if errorlevel 10 goto elevatedCaller
if errorlevel 1 goto failedCheck

rem Process-local compatibility only: no registry or system settings are edited.
rem Retain Windows 7 mode while requesting the caller's NORMAL privileges.
set "__COMPAT_LAYER=RunAsInvoker WIN7RTM"
pushd "%woffGameDir%" || goto failedDirectory
rem Deliberately do not wait: launch the game, then close this command window.
start "" "WOFF.exe"
if errorlevel 1 goto failedStart
popd
endlocal
exit /b 0

:missingGame
echo WOFF.exe was not found. Put Launch-WoFF.bat beside WOFF.exe.
echo Or pass your game folder in quotes as the first argument.
pause
exit /b 2
:missingResources
echo The game's resource folder is missing. No launch was attempted.
echo Check your installation. See README.md for help.
pause
exit /b 3
:missingAppId
echo steam_appid.txt is missing. No launch was attempted.
echo Copy the supplied steam_appid.txt beside WOFF.exe, ONLY if none exists.
echo Steam must be running under the account that owns the game.
pause
exit /b 4
:elevatedCaller
echo Double-click this launcher normally. Do NOT run it as administrator.
pause
exit /b 10
:alreadyRunning
echo WOFF is already running. Save and close it normally before trying again.
pause
exit /b 11
:missingSteam
echo Open Steam normally and sign into the account that owns the game, then retry.
pause
exit /b 12
:failedCheck
echo The read-only pre-launch checks failed. No launch was attempted.
pause
exit /b 13
:failedDirectory
echo Could not enter the game's folder. No launch was attempted.
pause
exit /b 14
:failedStart
popd
echo Windows could not start WOFF.exe. See README.md for troubleshooting.
pause
exit /b 15
