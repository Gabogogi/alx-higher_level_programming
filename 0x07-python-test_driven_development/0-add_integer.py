#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integer. casting them to integers if needed"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer".format(a))
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (int(a) + int(b))
