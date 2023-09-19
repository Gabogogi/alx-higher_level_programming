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

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

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
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
