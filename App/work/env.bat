@echo on
set REL_PATH=..\..\
pushd %REL_PATH%
set PYTHON=%CD%\python\python37
set PYTHONSCRIPTS=%CD%\python\python37\Scripts
set APP_PATH=App
pushd %APP_PATH%
set DEFAULTS=%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\

set PATH=%CD%;%PYTHON%;%PYTHONSCRIPTS%;%DEFAULTS%
echo PATH ENV = [%PATH%]
