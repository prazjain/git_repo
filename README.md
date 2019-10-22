# Automate Git workflow with Python
---

Programmed by praz.jain@gmail.com

Are you new to Git/github?

Creating a new repo can be quite tricky, and who wants to spend time fumbling around with source control when all you want to do is, get on with your actual coding. 

Creating a new repo is actually a few steps, to be followed in a sequence. (You need to create a remote repository (public/private?), then create a local repository, map local repository to remote repository etc)

How about if you can do this in seconds without having a crease on your brow?

##### Download the python scripts in this repo.

 * Make Python script executable

	`chmod +x git_repo.py`


### Usage

 * Create a repository

	`./git_repo.py create`

	 * It will ask you for the new repository name.
	 * It will ask if this is a private repository, ignore it for public repositories.
	 * It will create a remote repository in your account.
	 * It will create a local repository on your machine, in predefined path.
	 * It will add a readme.md file in local repository.
	 * It will map remote repository as origin, so push will cascade there.
	 * It will commit this initial checkin to local repository.
	 * It will push this initial checkin to remote repository.
	 * Opens up the code in IDE (All repos are wired up now for your coding to begin)

 * Use existing project and create/publish a repository

	`./git_repo.py existing`

	 * Same as create command except, it does not create local code directory (as reuses the one, that is present).
	 
 * Clone a repository 

	`./git_repo.py clone https://github.com/prazjain/Test3.git`

	 * This clones the repository to your machine, in predefined path.
	 * Opens up the code in IDE
	
 * Fork a repository

	`./git_repo.py fork https://github.com/Tyrrrz/CliWrap.git`

	 * It forks the 3rd party repository to your account.
	 * It creates your personal remote repository.
	 * It clones the remote respository to a predefined path.
	 * Any further commit go to your local repository.
	 * Any further push go to your personal remote repository.
	 * Opens up the code in IDE (All repositories are wired up now for your coding to begin)
	
 * More options coming...request them here


#### Sample Output from script


I created this repo using the script itself.

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

	
### Setup

##### Install latest python

[Python](https://www.python.org/downloads/)

##### Install Code editor

 * [PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=mac)

 * [Visual Studio Code](https://code.visualstudio.com/download)


##### Install pip

`sudo -H python -m ensurepip`

`pip install --upgrade pip`

##### Install PyGithub

`pip install PyGithub`



