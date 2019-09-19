#!/usr/bin/env python3

import sys
from GithubRepo import GithubRepo


def create():
    print("Creating repository...")
    repo = GithubRepo()
    repo.user_prompt()
    repo.create()
    print("Created repository")


def clone():
    print("clone option is unimplemented")


if __name__ == "__main__":
    option = sys.argv[1]
    if option == "create":
        create()
    elif option == "clone":
        clone()
    else:
        print("unsupported operation :" + option)
