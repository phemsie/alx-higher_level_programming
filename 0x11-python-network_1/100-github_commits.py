#!/usr/bin/python3
""" list 10 commits of the repository “rails” by the user “rails”"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    resp = requests.get(url)
    count = 0
    try:
        json_data = resp.json()
        for item in json_data:
            if count < 10:
                print("{}: {}".format(
                    item.get('sha'),
                    item['commit']['author'].get('name')))
                count += 1
    except valueError:
        print("Not a valid JSON")
