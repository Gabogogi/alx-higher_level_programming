#!/usr/bin/python3
'''
takes in a URL, sends a request
to the URL and displays the body of the response
'''
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
