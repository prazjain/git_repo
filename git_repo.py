#!/usr/bin/env python3

import sys
from repo.GithubRepo import GithubRepo


def create():
    print("Creating repository...")
    repo = GithubRepo()
    repo.user_prompt()
    repo.create()
    print("Created repository")


def existing():
    print("Creating repository...")
    repo = GithubRepo()
    repo.user_prompt(unique_local=False)
    repo.create(create_dir=False)
    print("Created repository")


def test():
    pass


def clone(url):
    repo = GithubRepo()
    repo.clone(url)


def fork(url):
    repo = GithubRepo()
    repo.fork(url)


if __name__ == "__main__":
    option = sys.argv[1].lower()
    if option == "create":
        create()
    elif option == "existing":
        existing()
    elif option == "clone":
        clone(sys.argv[2])
    elif option == "fork":
        fork(sys.argv[2])
    elif option == "test":
        test()
    else:
        print("unsupported operation :" + option)
