@echo off
>server.log (
call env.bat
python.exe init_server.py >> ..\Data\log_files\critical_error_server.log 2>&1
)
