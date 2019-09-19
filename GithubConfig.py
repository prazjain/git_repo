from Configuration import Configuration
import json


class GithubConfig(Configuration):
    def __init__(self):
        with open('configuration.json') as json_file:
            data = json.load(json_file)
            self._github_data = data["github"]
            self._base_dir = self._github_data["local_base_dir"]
            self._url = self._github_data["url"]
            self._ide_cmd = self._github_data["ide_cmd"]
