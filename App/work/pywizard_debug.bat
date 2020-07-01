@echo off
>pywizard.log (
call env.bat
python.exe pywizard.py >> ..\Data\log_files\pywizard_error.log 2>&1
)
