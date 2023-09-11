#!/usr/bin/python3

"""a class based on 6-base geometry"""


class BaseGeometry:
    """a class defining a shape"""

    def area(self):
        """raises exception since area is not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
