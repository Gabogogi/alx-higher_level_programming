#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]

    print("Max: {}".format(max_value))
