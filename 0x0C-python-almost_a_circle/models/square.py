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
        if args:
        # If positional arguments are provided, update attributes in order
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            # If no positional arguments, update attributes using keyword arguments
            for key, value in kwargs.items():
                setattr(self, key, value)      

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width)
