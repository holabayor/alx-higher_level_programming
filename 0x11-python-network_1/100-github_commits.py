#!/usr/bin/python3
'''
Script that list 10 commits (from the most recent to oldest)
of a repository
'''
import requests
import sys

if __name__ == '__main__':
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                              sys.argv[2])
    r = requests.get(url).json()
    for commit in r[:10]:
        print("{}: {}".format(commit['sha'],
                              commit['commit']['committer']['name']))
