#!/usr/bin/env python3

import sys
from GithubRepo import GithubRepo


def create():
    print("Creating repository...")
    repo = GithubRepo()
    repo.user_prompt()
    repo.create()
    print("Created repository")


def test(url):
    pass


def clone(url):
    repo = GithubRepo()
    repo.clone(url)


def fork(url):
    repo = GithubRepo()
    repo.fork(url)


if __name__ == "__main__":
    option = sys.argv[1]
    if option == "create":
        create()
    elif option == "clone":
        clone(sys.argv[2])
    elif option == "fork":
        fork(sys.argv[2])
    elif option == "test":
        test(sys.argv[2])
    else:
        print("unsupported operation :" + option)
