#!/usr/bin/python3
'''
Script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    headers = {"Authorization": "token {}".format(sys.argv[2])}
    r = requests.get(url, headers=headers).json()
    print(r.get('id'))
