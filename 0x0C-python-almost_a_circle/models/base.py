#!/usr/bin/python3


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialisation
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
