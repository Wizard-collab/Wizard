@echo off
set REL_PATH=..\
pushd %REL_PATH%
set PYTHON=%CD%\python27
set PYTHONSCRIPTS=%CD%\python27\Scripts
set DEFAULTS=%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\
set PATH=%CD%;%PYTHON%;%PYTHONSCRIPTS%;%DEFAULTS%
echo PATH ENV = [%PATH%]
