#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests
import sys


if __name__ == "__main__":
    username = 'Gabogogi'
    password = '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'

    api_url = 'https://api.github.com/user'
    response = requests.get(api_url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print("Error: {}".format(response.status_code))

