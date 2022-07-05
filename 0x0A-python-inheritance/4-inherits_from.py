#!/usr/bin/python3
"""
This module implements a function a that checks for inheritance
"""


def inherits_from(obj, a_class):
    """ Function that checks if the instance of an
    object is inherited from a specified class
    """
    return issubclass(type(obj), a_class)
