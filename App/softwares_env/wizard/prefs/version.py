from wizard.vars import defaults
import requests
from wizard.tools import reg_wizard
import json

class check_version():
    def __init__(self):
        self.last_version = self.get_last_version()
        self.current_version = defaults._wizard_version_

    def check_version(self):
        if self.last_version != self.current_version:
            return self.last_version
        else:
            return None

    def read_infos(self):

        infos = b''
        response = requests.get(defaults._infos_file_lk_, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            infos+=response.content
        else:
            for data in response.iter_content(chunk_size=4096):
                infos+=data

        return json.loads(infos.decode('utf-8'))

    def get_last_version(self):

        infos = self.read_infos()
        self.last_version = list(infos['Versions'].keys())[-1]
        self.last_version_setup_lk = infos['Versions'][self.last_version]['dl_link']
        self.file_name = infos['Versions'][self.last_version]['name']
        return self.last_version 