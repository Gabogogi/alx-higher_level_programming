#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    if int(idx) < 0 or int(idx) >= len(my_list):
        return my_list
    
    my_list[int(idx)] = new_element
    
    return print(my_list)
