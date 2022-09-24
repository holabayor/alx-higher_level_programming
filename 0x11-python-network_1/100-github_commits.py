#!/usr/bin/python3
'''
Script that list 10 commits (from the most recent to oldest)
of a repository
'''
import requests
import sys

if __name__ == '__main__':
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner,
                                                              repo)
    r = requests.get(url).json()
    for commit in r[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
