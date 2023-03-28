#!/usr/bin/python3
class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size=0):
        """Initialize method that stores the size of the square
        Args:
            param1 (int): size of the square
        """
        try:
            int(size)
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
