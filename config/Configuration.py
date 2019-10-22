"""Configuration object that represents value from JSON config file"""
import json


class Configuration:

    def __init__(self):
        # Defining variables here which will be set in sub classes
        self._base_dir = None
        self._url = None
        self._username = ''
        self._pwd = ''
        with open('configuration.json') as json_file:
            data = json.load(json_file)
            self._base_dir = data["local_base_dir"]
            self._ide_cmd = data["ide_cmd"]

    @property
    def base_dir(self):
        # Returns base dir on local machine where repositories will be created or cloned
        return self._base_dir

    @property
    def username(self):
        return self._username

    @property
    def pwd(self):
        return self._pwd

    @property
    def url(self):
        return self._url

    @property
    def ide_cmd(self):
        return self._ide_cmd
