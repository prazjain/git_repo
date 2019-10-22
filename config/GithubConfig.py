from config.Configuration import Configuration
import json


class GithubConfig(Configuration):
    def __init__(self):
        with open('configuration.json') as json_file:
            data = json.load(json_file)
            github_data = data['github']
            self._username = github_data['username']
            self._pwd = github_data['password']
            self._base_dir = github_data['local_base_dir']
            self._url = github_data['url']
            self._ide_cmd = github_data['ide_cmd']
