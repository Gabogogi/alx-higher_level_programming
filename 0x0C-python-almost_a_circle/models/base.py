#!/usr/bin/python3
'''Has the base class: 13 14 15'''
import json
import csv
import turtle


class Base:
    '''A base class for all the rest'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor'''
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns JSON string representation of dict'''
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes JSON string rep of list_objs to a file'''
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        list_of_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_of_dicts)
        with open(filename, "w") as file:
            file.write(json_string)

    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_of_dicts = json.loads(json_string)
                instances = [cls.create(**d) for d in list_of_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes and saves instances to a CSV file'''
        filename = "{}.csv".format(cls.__name__)

        with open(filename, 'w') as file:
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    file.write("{},{},{},{},{}\n".format(
                        obj.id, obj.width, obj.height, obj.x, obj.y))
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    file.write("{},{},{},{}\n".format(
                        obj.id, obj.size, obj.x, obj.y))

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes and loads instances from a CSV file'''
        filename = "{}.csv".format(cls.__name__)

        instances = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    values = line.strip().split(',')
                    if cls.__name__ == 'Rectangle':
                        instance = cls(int(values[1]), int(values[2]),
                                       int(values[3]), int(values[4]),
                                       int(values[0]))
                    elif cls.__name__ == 'Square':
                        instance = cls(int(values[1]), int(values[2]),
                                       int(values[3]), int(values[0]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
