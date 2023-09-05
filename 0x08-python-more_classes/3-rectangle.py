#!/usr/bin/python3

"""
Defines a rectangle with height and width
"""


class Rectangle:

    """defines a rectangle by: (based on 0-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """Instantiates rectangle optional width and height

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width

        Returns:
            _int_: Width of the rectangle
        """        """"""
        return self.__width

@width.setter
    def width(self, width):
        """Sets width of rectangle

        Args:
            width (int)

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """gets height of rectangle

        Returns:
            int: height of rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, height):
        """sets height of the rectangle

        Args:
            height (int): height of rectangle

        Raises:
            TypeError: if height is is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.width
    

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)


    def __str__(self) -> str:
        """Returns a string representation of rectangle with hash"""
        if self.__height == 0 or self.__width == 0:
            return ""    
        result = ""
        for i in range(self.height):
            result += "#" * self.width + "\n"
        return result.rstrip()
