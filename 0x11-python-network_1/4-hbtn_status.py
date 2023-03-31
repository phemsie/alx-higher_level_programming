#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status
using requests
"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("	- type:", type(r.text))
    print("	- content:", r.text)
