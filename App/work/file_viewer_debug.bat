@echo off
>file_viewer.log (
call env.bat
python.exe file_viewer.py >> ..\Data\log_files\file_viewer_error.log 2>&1
)
