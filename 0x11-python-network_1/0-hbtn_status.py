#!/usr/bin/python3
""" A script  that fetches https://alx-intranet.hbtn.io/status
using urllib and displays the body of the response
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        html_body = r.read()

    print("Body response:")
    print("\t- type:", type(html_body))
    print("\t- content:", html_body)
    print("\t- utf8 content:", html_body.decode('utf-8'))
