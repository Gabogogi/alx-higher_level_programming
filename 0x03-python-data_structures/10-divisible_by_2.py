#!/usr/bin/python3
def divisible_by_2(my_list=[]):    
    new_div = []
    for i in my_list:
        if i % 2 == 0:
            new_div.append(True)
        else:
            new_div.append(False)
    return new_div
