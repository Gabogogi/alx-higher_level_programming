#!/usr/bin/python3
'''Rectangle which inherits from square'''
from models.base import Base


class Rectangle(Base):
    '''A rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''setter for width'''
        if type(width) is int:
            if width <= 0:
                raise ValueError('width must be > 0')
            else:
                self.__width = width
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, height):
        '''setter for height'''
        if type(height) is int:
            if height <= 0:
                raise ValueError('height must be > 0')
            else:
                self.__height = height
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''setter for x'''
        if type(x) is int:
            if x < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = x
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''setter for y'''
        if type(y) is int:
            if y < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = y
        else:
            raise TypeError('y must be an integer')

    def area(self):
        '''computes rectangle area'''
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    
    def update(self, *args, **kwargs):
        """Update the Rectangle"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    
    def to_dictionary(self):
        '''returns dictionary rep of rectangle'''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'width': self.__width, 'height': self.__height}

    def __str__(self):
        '''string representation'''
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)
