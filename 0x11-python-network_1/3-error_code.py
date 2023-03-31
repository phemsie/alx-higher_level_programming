#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response  """
import sys
import urllib.request
from urllib import parse
from urllib import error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url=sys.argv[1]) as response:
            data = response.read()
            data = data.decode('utf-8')
            print(data)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
