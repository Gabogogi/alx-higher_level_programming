#!/usr/bin/python3

"""Checks if object is an instnace of, or the object is inherited
from a class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance o a class"""
     if isinstance(obj, a_class):
        return True
    return False
