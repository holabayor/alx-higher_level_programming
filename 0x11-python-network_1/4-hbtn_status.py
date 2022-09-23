#!/usr/bin/python3
'''
Script that fetches https://alx-intranet.hbtn.io/status
'''
import requests

if __name__ == '__main__':
    r = requests.get("https://alx-intranet.hbtn.io/status")
    body = r.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
