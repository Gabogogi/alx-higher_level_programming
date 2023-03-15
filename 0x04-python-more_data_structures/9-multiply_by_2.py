#!/usr/bin/python3

def multiply_values_by_2(d):
    new_d = {}
    for key, value in d.items():
        new_d[key] = value * 2
    return new_d
