#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if int(idx) < 0 or int(idx) >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list[int(idx)] = element
    return new_list
