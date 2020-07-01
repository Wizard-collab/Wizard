import winreg
from wizard.vars import defaults

KEY = defaults._reg_key_

def get_installed_version():

    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE , KEY, 0, winreg.KEY_ALL_ACCESS)
        print(registry_key)
        install_path, _null = winreg.QueryValueEx(registry_key, 'DisplayVersion')
        winreg.CloseKey(registry_key)
        if install_path:
            return install_path
        else:
            return None
    except WindowsError as e: 
        print(e)
        return None
    