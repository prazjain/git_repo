"""Implements functionality to interact with Github repos"""
from GithubConfig import GithubConfig
from Repo import Repo
import os
from github import Github


class GithubRepo(Repo):

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
        git_config = GithubConfig()
        print("Connecting to server with your credentials")
        uname_pwd = git_config.username_pwd()
        ghub = Github(uname_pwd[0], uname_pwd[1])
        cwd = git_config.base_dir() + "/" + self._repo_name
        #make dirs in this path
        os.makedirs(cwd)
        #change current working dir to this new repo
        os.chdir(cwd)

        #create remote repo
        user = ghub.get_user()
        repo = user.create_repo(self._repo_name, private=self._private)
        print("Successfully created remote repository :" + self._repo_name)
        #create local repo
        print("Creating local repository :" + self._repo_name + ", in " + cwd)
        os.system("git init")
        new_repo_git = git_config.url() + "/" + self._repo_name + ".git"
        os.system("git remote add origin " + new_repo_git)
        os.system("touch README.md")
        os.system("git add .")
        os.system("git commit -m 'Initial Commit'")
        os.system("git push -u origin master")
        print("Created local repository")
        os.system(git_config.ide_cmd())
