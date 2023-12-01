#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    w = requests.get(url)
    
    if w.status_code >= 400:
        print("Error code: {}".format(w.status_code))
    else:
        print(w.text)


