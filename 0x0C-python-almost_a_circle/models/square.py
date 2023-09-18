#!/usr/bin/python3
'''Contains square class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''square that inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''square constructor'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for width'''
        return self.width

    @size.setter
    def size(self, size):
        '''setter for size'''
        if type(size) is int:
            if size < 0:
                raise ValueError('width must be > 0')
            else:
                self.width = size
                self.height = size
        else:
            raise TypeError('width must be an integer')

    def to_dictionary(self):
        '''returns dictionary rep of square'''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.width}

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.width)
