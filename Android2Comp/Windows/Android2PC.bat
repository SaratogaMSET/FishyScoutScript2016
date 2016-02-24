setlocal enabledelayedexpansion
set outputDir=
:start
title ADB Tester
@echo off
ECHO i INPUT
ECHO o OUTPUT
ECHO a ADB
@echo off
IF "%~1"=="-i" set inputDir=%2
IF "%~3"=="-o" set outputDir=%4
IF "%~5"=="-a" GOTO a
SET inputDir=%2
SET outputDir=%4
echo New input directory is !inputDir!
PAUSE  
mkdir !outputDir!
mkdir !outputDir!\output      
echo New output directory is !outputDir!
PAUSE
echo.
:a       
echo Ready to use ADB commands.
PAUSE
echo.
echo Showing currently connected ADB devices. Serial number first, then status.
PAUSE
adb devices
echo.
adb get-serialno
!serialno!
@echo on
@echo !SERIALNO!
adb pull !inputDir!/scoutNotes.txt !outputDir!
PAUSE
echo.
echo Pulled from the input Directory !inputDir! and pushed to the output Directory !outputDir!.
PAUSE
echo Exiting Command Line
PAUSE
echo Clearing Space
PAUSE
clear
EXIT /B no