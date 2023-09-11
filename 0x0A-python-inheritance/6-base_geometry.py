#!/usr/bin/python3

"""a class based on 5-base geometry"""


class BaseGeometry:
    """a class defining a shape"""

    def area(self):
        """raises exception since area is not defined"""
        raise Exception("area() is not implemented")
