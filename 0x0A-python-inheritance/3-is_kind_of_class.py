#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a given class.
"""

def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of the given class."""
    return isinstance(obj, a_class)
