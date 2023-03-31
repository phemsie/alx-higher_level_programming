#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
import sys
import requests


if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    if (html.status_code >= 400):
        print("Error code: {}".format(html.status_code))
    else:
        print(html.text)
