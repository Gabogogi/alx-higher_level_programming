#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    r = requests.post(url, data=data)
    print(r.text)