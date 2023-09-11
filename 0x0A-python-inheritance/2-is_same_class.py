#!/usr/bin/python3

"""Checks exact class"""

def is_same_class(obj, a_class):
    """ function that returns True if the object is
    exactly an instance of the specified class ; otherwise False"""
    return obj.__class__ is a_class
