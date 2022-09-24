#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL
and displays the body of the response
'''
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    code = r.status_code
    print(r.text) if code < 400 else print("Error code: {}".format(code))
