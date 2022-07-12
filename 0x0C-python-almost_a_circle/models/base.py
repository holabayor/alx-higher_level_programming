#!/usr/bin/python3
""" This module implements the Base Class of all other classes used in this
project.
"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of Base object"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts to a json string """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves json to a file """
        rects = []
        squares = []
        for i in list_objs:
            if i.__class__.__name__ == "Rectangle":
                rects.append(i.to_dictionary())
            elif i.__class__.__name__ == "Square":
                squares.append(i.to_dictionary())
        if rects:
            with open("Rectangle.json", "w") as f:
                f.write(Base.to_json_string(rects))
        if squares:
            with open("Square.json", "w") as f:
                f.write(Base.to_json_string(squares))

    @staticmethod
    def from_json_string(json_string):
        """ changes from json to a list """
        if not json_string or json_string is not None:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance with all the attributes already set """
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)
        instances = []
        with open(filename, "r") as f:
            file_list = Base.from_json_string(f.read())
            for _list in file_list:
                instances.append(cls.create(**_list))
        return instances
