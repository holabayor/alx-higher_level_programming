#!/usr/bin/python3
"""
This module implements a function a that checks for subclasses
"""


def is_kind_of_class(obj, a_class):
    """ Function that checks if an object is a subclass
    of a specified class
    """
    return issubclass(obj, a_class)
