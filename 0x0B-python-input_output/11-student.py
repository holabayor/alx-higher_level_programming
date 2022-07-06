#!/usr/bin/python3
""" Student module
"""


class Student:
    """ Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization

        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        json_dict = self.__dict__
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            json_dict = {}
            try:
                for k, v in self.__dict__.items():
                    if k in attrs:
                        json_dict[k] = v
            except KeyError:
                pass
        return json_dict

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
