#!/usr/bin/python3
""" Searches, sends a POST request to with the letter as a parameter """
import sys
import requests


if __name__ == "__main__":
    search = ""
    if len(sys.argv) > 1:
        search = sys.argv[1]
    html = requests.post('http://0.0.0.0:5000/search_user', data={'q': search})
    try:
        json_data = html.json()
        if len(json_data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
