"""Implements functionality to interact with Github repos"""

from config.GithubConfig import GithubConfig
from repo.Repo import Repo
import os
from github import Github, UnknownObjectException
import pathlib
from config.FilePathUtils import FilePathUtils
import shutil
import sys


class GithubRepo(Repo):

    def __init__(self):
        super().__init__()
        self._git_config = GithubConfig()
        print("Connecting to server with your credentials")
        self._ghub = Github(self._git_config.username, self._git_config.pwd)

    def user_prompt(self, unique_local=True):
        # As user for any / all options wrt creation of this repo type
        self._repo_name = self._get_unique_repo_name(unique_local)
        private = input("Is this private repo (yes/y) :").lower()
        self._private = True if private == "y" or private == "yes" else False
        comment = input('Checkin comment :')
        self._comment = 'Initial Comment' if not comment else comment

    def _create_local_repo(self, create_dir=True):
        lang = input('Primary language of the project (java/python) :').lower()
        lang = lang if lang == 'java' or lang == 'python' else ''
        source_path = self._filePathUtils.gitignore_file(lang)
        assert os.path.abspath(source_path)

        self._cwd = self._git_config.base_dir + "/" + self._repo_name
        # make dirs in this path
        if create_dir:
            os.makedirs(self._cwd)

        # change current working dir to this new repo
        os.chdir(self._cwd)

        # create local repo
        print("Creating local repository :" + self._repo_name + ", in " + self._cwd)
        try:
            shutil.copy(source_path, self._cwd + "/.gitignore")
        except IOError as e:
            print("Unable to copy git ignore file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

        os.system("git init")
        os.system("touch README.md")
        os.system("git add .")
        os.system(f"git commit -m '{self._comment}'")
        print("Created local repository")

    def _create_remote_repo(self):
        user = self._ghub.get_user()
        repo = user.create_repo(self._repo_name, private=self._private)
        print("Successfully created remote repository :" + self._repo_name)

    def _map_local_to_remote_repo(self, push_changes=True):
        new_repo_git = self._git_config.url + "/" + self._repo_name + ".git"
        os.system("git remote add origin " + new_repo_git)
        if push_changes:
            os.system("git push -u origin master")
        print('Mapped repo and pushed changes to remote')
        pass

    def create(self, create_dir=True):
        self._create_local_repo(create_dir)
        self._create_remote_repo()
        self._map_local_to_remote_repo()
        os.system(self._git_config.ide_cmd)

    # This method is to publish existing code to github. Code dir should be present in pre-configured location
    def clone(self, url):
        # url format is : https://github.com/prazjain/Test3.git
        print("Cloning a repository")
        # change current working dir to this new repo
        os.chdir(self._git_config.base_dir)
        # clone this to local machine
        os.system("git clone " + url)
        self._repo_name = url.split("/")[-1].replace(".git", "")
        print("Repo name is : " + self._repo_name)
        # update cwd
        self._cwd = self._git_config.base_dir + "/" + self._repo_name
        os.chdir(self._cwd)
        os.system(self._git_config.ide_cmd)

    def fork(self, url):
        # url format is : https://github.com/prazjain/Test3.git
        print("Forking a repository")
        # fork remote repo
        user = self._ghub.get_user()
        repo_name = url.split("/")[-2] + "/" + url.split("/")[-1].replace(".git", "")
        fork_repo = user.create_fork(self._ghub.get_repo(repo_name))
        self.clone(fork_repo.clone_url)

    def pull_request(self, comment):
        os.system("git add .")
        os.system("git commit -m '" + comment + "'")
        os.system("git push -u origin master")

    def _get_unique_repo_name(self, unique_local):
        name = ''
        while True:
            name = input('Enter unique repo name : ')
            if unique_local:
                local_dir = self._git_config.base_dir + "/" + name
                if pathlib.Path(local_dir).exists():
                    print(f'{name} already exists in {self._git_config.base_dir}')
                    continue
            # check no remote repo exists with same name
            user = self._ghub.get_user()
            try:
                repo = user.get_repo(name)
                if repo:
                    print(f'{name} already exists in remote repository {self._git_config.url}')
                    continue
            except UnknownObjectException as uoe:
                # If repo does not exist, we will get 404 message here
                pass
            break
        return name
