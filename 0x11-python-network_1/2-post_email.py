#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request  """
import sys
import urllib.request
from urllib import parse


if __name__ == "__main__":
    post_data = parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=sys.argv[1], data=post_data) as response:
        data = response.read()
        data = data.decode('ascii')
        print(data)
