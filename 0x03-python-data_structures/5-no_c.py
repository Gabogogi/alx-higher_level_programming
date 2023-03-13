#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    c = ["C", "c"]
    for char in my_string:
        if char not in c:
            new_string += char
    return new_string
