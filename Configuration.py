"""Configuration object that represents value from JSON config file"""
import json


class Configuration:

    def __init__(self):
        # Defining variables here which will be set in sub classes
        self._github_data = ("", "")
        self._base_dir = None
        self._url = None
        with open('configuration.json') as json_file:
            data = json.load(json_file)
            self._base_dir = data["local_base_dir"]
            self._ide_cmd = data["ide_cmd"]

    def base_dir(self):
        # Returns base dir on local machine where repositories will be created or cloned
        return self._base_dir

    def username_pwd(self):
        # Returns a tuple with username and password
        return self._github_data["username"], self._github_data["password"]

    def url(self):
        return self._url

    def ide_cmd(self):
        return self._ide_cmd
