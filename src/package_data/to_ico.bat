@echo off
REM Start convertion
echo "Start icon conversion using Imagick on Windows."
magick.exe convert %1 -define icon:auto-resize=256 -compress zip icon.ico
