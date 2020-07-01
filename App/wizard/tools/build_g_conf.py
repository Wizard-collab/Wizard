from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
import os

prefs = prefs()

logger = log.pipe_log()

def get_conf_file(python_paths):
    project_path = prefs.project_path
    conf_file = os.path.join(project_path, defaults._guerilla_conf_file_)
    conf_data = get_data(python_paths)
    write_conf(conf_file, conf_data)
    print(conf_data)
    return conf_file


def get_data(python_paths):
    logger.info(python_paths)
    conf_data = '# Broadcast guerilla.conf file created by wizard\n'
    conf_data += 'UserLibrary = {}'.format(python_paths[0].replace('\\', '/'))
    python_paths.pop(0)
    for path in python_paths:
        conf_data += ';'
        conf_data += path.replace('\\', '/')
    #python_path = os.path.abspath('..\\python')
    #python27_path = (python_path + '\\python27\\python27.dll').replace('\\', '/')
    #conf_data += '\nPythonLibrary = {}'.format(python27_path)
    return conf_data


def write_conf(conf_file, conf_data):
    with open(conf_file, 'w') as f:
        f.write(conf_data)
