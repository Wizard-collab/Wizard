=====================
Setup the environment
=====================

To use wizard with the correct python environment, you need to use the Python 3.7 given with the install

The Python.exe file is located here : $INSTALLDIR/Wizard/Python/python37/python.exe

You will also need to set the "App" path as the current directory::

	import sys
	import os

	app_path = os.path.abspath("../../App")
	os.chdir(app_path)

You will need to do that only if you want to use Wizard from the command line, else, if you are using the Wizard Gui App ( Wizard.exe ), the environment is automatically setted. It is done by a .bat file ( init.bat ) located here : $INSTALLDIR/Wizard/App/bat/wizard.bat::

	@echo off
	>main_ui.log (
	call env.bat
	python.exe __init__.py
	)

It calls the file env.bat::
	
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

If you only want to use wizard from the command line, you will need to create an environment on the fly using the "defaults" wizard module::

	from wizard.vars import defaults
	import os

	os.environ[defaults._site_var_] = os.path.abspath(defaults._site_)
	os.environ[defaults._abs_site_path_] = os.path.abspath('')
	os.environ[defaults._stats_var_] = os.path.abspath(defaults._stats_)
	os.environ[defaults._project_db_env_] = ''
	os.environ[defaults._current_assets_list_] = ''

So, in order to use wizard without GUI, here is the full environment setup script::

	>>> import sys
	>>> import os
	>>> app_path = os.path.abspath("../../App")
	>>> os.chdir(app_path)
	>>> from wizard.vars import defaults
	>>> os.environ[defaults._site_var_] = os.path.abspath(defaults._site_)
	>>> os.environ[defaults._abs_site_path_] = os.path.abspath('')
	>>> os.environ[defaults._stats_var_] = os.path.abspath(defaults._stats_)
	>>> os.environ[defaults._project_db_env_] = ''
	>>> os.environ[defaults._current_assets_list_] = ''