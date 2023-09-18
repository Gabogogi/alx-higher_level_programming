#!/usr/bin/python3
'''Rectangle which inerits from square'''
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
            if width < 0:
                raise ValueError('width must be >= 0')
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
            if height < 0:
                raise ValueError('height must be >= 0')
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
        '''returns rectangle representation'''
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        '''Update attrs based on pos and keyword args'''
        if args:
            # If pos args, update attributes in order
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            # update attrs using keyword args, if no keyword args
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns dictionary rep of rectangle'''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'width': self.__width, 'height': self.__height}

    def __str__(self):
        '''string representation'''
        return "[{}] ({}) {}/{}  - {}/{}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)
