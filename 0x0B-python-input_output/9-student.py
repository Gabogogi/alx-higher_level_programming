#!/usr/bin/python3
'''
contains student class
'''


class Student:
    '''representations of a class'''
    def __init__(self, first_name, last_name, age):
        '''instantiates a class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves dictionary rep of student'''
        return self.__dict__

