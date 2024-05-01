#!/usr/bin/python3

""" A script that fetches https://alx-intranet.hbtn.io/status
using  the package requests
"""
import requests

if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)
