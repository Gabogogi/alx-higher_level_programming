#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end='')
        except (ValueError, TypeError):
            continue
        else:
            i += 1
    print()
    return i
