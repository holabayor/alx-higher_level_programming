#!/usr/bin/python3
"""
This module implements base geometry class
"""


class BaseGeometry:
    """ Base Geometry class
    """
    def area(self):
        """ Raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value input
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
