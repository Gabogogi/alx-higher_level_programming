#!/usr/bin/python3

"""a class based on 8-base geometry"""


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


class Rectangle(BaseGeometry):
    """defines a rectangle from geometry class"""
    def __init__(self, width, height):
        """initializes a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self, width, height):
        """implements area function"""
        self.area = self.width * self.height

    def __str__(self):
        """sring function"""
        return "[{}] {}/{}".format(self.__class.__.__name__,
         self.width, self.height)
