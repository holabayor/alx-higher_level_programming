#!/usr/bin/python3
'''
Script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    data = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(data).encode("ascii")
    print(data)
    with urllib.request.urlopen(sys.argv[1], data) as response:
        body = response.read()
        #print(body.decode('utf-8'))
