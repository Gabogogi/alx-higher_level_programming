#!/usr/bin/python3
def element_at(my_list, idx):
    if int(idx) < 0 or int(idx) > len(my_list):
        return None

    return print("Element at index {:d} is {}".format(int(idx), my_list[int(idx)]))
