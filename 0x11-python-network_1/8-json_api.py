#!/usr/bin/python3
'''
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    arg = ""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    data = {'q': '{}'.format(arg)}
    try:
        r = requests.post(url, data=data).json()
        if not r:
            print('No result')
        else:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
    except ValueError:
        print('Not a valid JSON')
