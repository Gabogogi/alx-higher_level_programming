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
        return self.__size

    @size.setter
    def size(self, size):
        '''setter for size'''
        if type(size) is int:
            if size < 0:
                raise ValueError('width must be >= 0')
            else:
                self.width = size
                self.width = size
        else:
            raise TypeError('width must be an integer')

    def to_dictionary(self):
        '''returns dictionary rep of square'''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.width}

    def __str__(self):
        '''string representation'''
        return "[{}] ({}) {}/{}  - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height)
