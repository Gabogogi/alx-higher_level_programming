#!/usr/bin/python3

"""Checks if object is an instnace of, or the object is inherited
from a class"""

def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class
    """
    return isinstance(obj, a_class)
