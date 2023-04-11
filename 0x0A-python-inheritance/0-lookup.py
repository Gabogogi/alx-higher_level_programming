#!/usr/bin/python3
"""
This module provides a function for looking up the available attributes"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
