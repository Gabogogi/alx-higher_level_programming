#!/usr/bin/python3
'''
adds all argmuments to a list and loads them to json file
'''


from sys import argv
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    json_list = load_from_json(filename)
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json(json_list, filename)
