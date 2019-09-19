"""Generic interface to interact with any repository (Github, Bitbucket etc)"""


class Repo:

    def __init__(self):
        self._repo_name = ""
        self._private = False

    def user_prompt(self):
        pass

    def create(self):
        pass
