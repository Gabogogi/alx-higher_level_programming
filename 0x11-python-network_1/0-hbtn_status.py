#!/usr/bin/python3
'''
A Python script that fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        print(response.status)