#!/usr/bin/python3
'''
displays the value of the X-Request-Id variable found in the header of the
response
'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = response.getheaders()
        for tup in headers:
            if 'X-Request-Id' in tup:
                print(tup[1])
