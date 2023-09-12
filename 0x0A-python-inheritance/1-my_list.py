#!/usr/bin/python3
'''
Contains a class MyList
'''


class MyList(list):
    '''
    A class that inherits from list
    '''
    def __init__(self):
        '''initializes the object'''
        super().__init__()

    def print_sorted(self):
        '''that prints the list, but sorted'''
        print(sorted(self))
