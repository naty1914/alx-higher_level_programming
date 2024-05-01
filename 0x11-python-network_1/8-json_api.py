#!/usr/bin/python3

""" A script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    data = {'q': letter}
    res = requests.post(url, data=data)
    try:
        result = res.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
