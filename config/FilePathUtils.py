import os


class FilePathUtils:

    def __init__(self):
        self._root = os.getcwd()

    @property
    def configuration_file(self):
        return '{}/configuration.json'.format(self._root)

    def gitignore_file(self,prefix):
        return '{}/gitignores/{}.gitignore'.format(self._root, prefix)
