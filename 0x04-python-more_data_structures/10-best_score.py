#!/usr/bin/python3

def best_score(a_dictionary):
    max_val = 0
    for x in a_dictionary.values():
        if max_val < x:
            max_val = x
    key_list = list(newdict.keys())
    val_list = list(newdict.values())
    pos = val_list.index(max_val)
    res = key_list[pos]
    return res
