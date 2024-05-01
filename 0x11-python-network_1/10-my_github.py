#!/usr/bin/python3
""" A script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                            sys.argv[2]))
    response_result = response.json()
    print(response_result.get('id'))
