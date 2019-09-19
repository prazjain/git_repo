"""Implements functionality to interact with Github repos"""
from GithubConfig import GithubConfig
from Repo import Repo
import os
from github import Github


class GithubRepo(Repo):

    def __init__(self):
        self._git_config = GithubConfig()
        print("Connecting to server with your credentials")
        uname_pwd = self._git_config.username_pwd()
        self._ghub = Github(uname_pwd[0], uname_pwd[1])

    def user_prompt(self):
        #As user for any / all options wrt creation of this repo type
        self._repo_name = input("Enter repo name :")
        private = input("Is this private repo (Yes/yes/Y/y) :")
        if private == "Yes" or private == "Y" or private == "y" or private == "yes":
            self._private = True
        else:
            self._private = False

    def create(self):
        #create local repo, then create remote repo

        self._cwd = self._git_config.base_dir() + "/" + self._repo_name
        #make dirs in this path
        os.makedirs(self._cwd)
        #change current working dir to this new repo
        os.chdir(self._cwd)

        #create remote repo
        user = self._ghub.get_user()
        repo = user.create_repo(self._repo_name, private=self._private)
        print("Successfully created remote repository :" + self._repo_name)
        #create local repo
        print("Creating local repository :" + self._repo_name + ", in " + self._cwd)
        os.system("git init")
        new_repo_git = self._git_config.url() + "/" + self._repo_name + ".git"
        os.system("git remote add origin " + new_repo_git)
        os.system("touch README.md")
        os.system("git add .")
        os.system("git commit -m 'Initial Commit'")
        os.system("git push -u origin master")
        print("Created local repository")
        os.system(self._git_config.ide_cmd())

    def clone(self, url):
        # url format is : https://github.com/prazjain/Test3.git
        print("Cloning a repository")
        # change current working dir to this new repo
        os.chdir(self._git_config.base_dir())
        # clone this to local machine
        os.system("git clone " + url)
        self._repo_name = url.split("/")[-1].replace(".git", "")
        print("Repo name is : " + self._repo_name)
        # update cwd
        self._cwd = self._git_config.base_dir() + "/" + self._repo_name
        os.chdir(self._cwd)
        os.system(self._git_config.ide_cmd())

    def fork(self, url):
        # url format is : https://github.com/prazjain/Test3.git
        print("Forking a repository")
        #fork remote repo
        user = self._ghub.get_user()
        repo_name = url.split("/")[-2] + "/" + url.split("/")[-1].replace(".git", "")
        fork_repo = user.create_fork(self._ghub.get_repo(repo_name))
        self.clone(fork_repo.clone_url)
