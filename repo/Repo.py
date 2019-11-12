"""Generic interface to interact with any repository (Github, Bitbucket etc)"""
from config.FilePathUtils import FilePathUtils


class Repo:

    def __init__(self):
        self._repo_name = ""
        self._private = False
        self._filePathUtils = FilePathUtils()

    def user_prompt(self):
        pass

    def create(self):
        pass
