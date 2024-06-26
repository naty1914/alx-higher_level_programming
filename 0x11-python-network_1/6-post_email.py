#!/usr/bin/python3

""" A script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response
"""
import requests
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=values)
    print(res.text)
