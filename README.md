# Automate Git workflow with Python
---

Programmed by praz.jain@gmail.com

Are you new to Git/github?

Creating a new repo can be quite tricky, and who wants to spend time fumbling around with source control when all you want to do is, get on with your actual coding. 

Creating a new repo is actually a few steps, to be followed in a sequence. (You need to create a remote repository (public/private?), then create a local repository, map local repository to remote repository etc)

How about if you can do this is seconds without having a crease on your brow?

###Setup

#####Install latest python

[Python](https://www.python.org/downloads/)

#####Install Code editor

 * [PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=mac)

 * [Visual Studio Code](https://code.visualstudio.com/download)


#####Install pip

`sudo -H python -m ensurepip`

`pip install --upgrade pip`

#####Install PyGithub

`pip install PyGithub`

#####Download the python scripts in this repo.

 * Make Python script executable

	`chmod +x git_repo.py`

 * Create a repo

	`./git_repo.py create`

	In next steps, the script will ask you for repository name, and whether you want to create a private repo.

	Once the repo is created, it will open the directory in your favourite editor (PyCharm / Visual Studio Code) as configured.

 * Clone a repo

	`./git_repo.py clone`

	I will implement this soon.

#####Sample

I created this repo using this script itself.

    (venv) Prashants-MacBook-Pro:hello Prashant$ ./git_repo.py create
    Creating repository...
    Enter repo name :git_repo
    Is this private repo (Yes/yes/Y/y) :
    Connecting to server with your credentials
    Successfully created remote repository :git_repo
    Creating local repository :git_repo, in /local/data/github/git_repo
    Initialized empty Git repository in /LOCAL/Data/github/git_repo/.git/
    [master (root-commit) 0ea6283] Initial Commit
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 README.md
    Counting objects: 3, done.
    Writing objects: 100% (3/3), 219 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/prazjain/git_repo.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    Created local repository
    Created repository
    (venv) Prashants-MacBook-Pro:hello Prashant$ 

Update the configuration.json file with url to your github repository and your username and password.

