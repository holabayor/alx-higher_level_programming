#!/usr/bin/python3
'''
Script that fetches https://alx-intranet.hbtn.io/status
'''
import requests
import sys

if __name__ == '__main__':
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
