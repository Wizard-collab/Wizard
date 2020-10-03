@echo off
>distribute.log (
call env.bat
python.exe distribute.py >> ..\Data\log_files\distribute.log 2>&1
)
