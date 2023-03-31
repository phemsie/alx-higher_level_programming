#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    html = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(html.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
