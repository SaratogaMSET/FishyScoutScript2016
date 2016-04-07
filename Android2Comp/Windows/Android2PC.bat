setlocal enabledelayedexpansion
set inputDir=
set outputDir=
:start
title Team 649 M-SET Fish: Android Debug Bridge
@echo off
REM CHECK FOR FOLDER TRANSMIT.
IF "%~1"=="-f" GOTO transmit
REM set to commands.
IF "%~1"=="-i" set inputDir=/sdcard/Notes
IF "%~2"=="-o" goto checkParam3
:checkParam3
SET inputDir=/sdcard/Notes
SET outputDir=C:\Python27\FishyScoutScript2016
echo New input directory is !inputDir!
PAUSE  
echo New output directory is in the FishyScoutScript2016 folder, located in the Python27 folder in the C drive.
PAUSE
echo.
IF "%~3"=="-a" GOTO a
:a
echo Ready to use ADB commands.
PAUSE
adb devices
adb pull !inputDir! !outputDir!
PAUSE
echo.
echo Pulled from the input Directory !inputDir! and pushed to the output Directory !outputDir!.
PAUSE
cls
GOTO end
:transmit
title Folder Transmitter
adb push C:\Python27\FishyScoutScript2016\Categories /sdcard/Categories
echo pushed Categories
adb push C:\Python27\FishyScoutScript2016\teamNumbers /sdcard/teamNumbers
echo pushed teamNumbers
PAUSE
:end
