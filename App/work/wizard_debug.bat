@echo off
>main_ui.log (
call env.bat
python.exe wizard_site.py >> ..\Data\log_files\critical_error.log 2>&1
)
