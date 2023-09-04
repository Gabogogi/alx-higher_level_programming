#!/usr/bin/python3

"""
Defines a rectangle with height and width
"""


class Rectangle:


    """defines a rectangle by: (based on 0-rectangle.py)"""


    number_of_instances = 0
    print_symbol = "#"
    
  
    def __init__(self, width=0, height=0):
        """Instantiates rectangle optional width and height"""        
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1


    def __del__(self):
        """delete class instance"""       
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1 


    @property
    def width(self):
        """getter for width"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """Sets width of rectangle"""
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
        """sets height of the rectangle"""
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
            result += str(self.print_symbol) * self.width + "\n"
            result += "{}\n".format(str(self.print_symbol) * self.width)
        return result.rstrip()
    
    
    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
