#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        charset = html.decode('utf-8')
        print("Body response:")
        print(
            "\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
            .format(type(html), html, charset))
