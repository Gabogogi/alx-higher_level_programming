#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    for x in val_list:
        if x == value:
            pos = val_list.index(value)
            to_remove = key_list[pos]
            a_ary.pop(to_remove, None)
    return a_dictionary
