import os
import shutil
from wizard.vars import defaults
from wizard.tools import log

logger = log.pipe_log()


def setup_guerilla(exe):
    install_dir = os.path.dirname(exe)
    add_python_zip(install_dir)
    add_python_dll(install_dir)
    add_python_DLLs(install_dir)


def add_python_zip(install_dir):
    python_zip_file = os.path.abspath(defaults._python_27_zip_)
    guerilla_python26_zip_file = os.path.join(install_dir, defaults._guerilla_python26_zip_)
    guerilla_python27_zip_file = os.path.join(install_dir, defaults._guerilla_python27_zip_)

    if os.path.isfile(guerilla_python26_zip_file):
        try:
            os.remove(guerilla_python26_zip_file)
        except PermissionError:
            logger.warning("You don't have the permission to access the guerilla install")
    if not os.path.isfile(guerilla_python27_zip_file):
        try:
            shutil.copy(python_zip_file, guerilla_python27_zip_file)
        except PermissionError:
            logger.warning("You don't have the permission to access the guerilla install")


def add_python_dll(install_dir):
    python_dll_file = os.path.abspath(defaults._python_27_dll_)
    guerilla_python26_dll_file = os.path.join(install_dir, defaults._guerilla_python26_dll_)


def add_python_DLLs(install_dir):
    python_DLLs_folder = os.path.abspath(defaults._python_27_DLLs_)
    guerilla_python26_DLLs_folder = os.path.join(install_dir, defaults._guerilla_python26_DLLs_)
