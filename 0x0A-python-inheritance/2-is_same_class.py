#!/usr/bin/python3
"""
This module implements a function a that checks the instance of an object
"""


def is_same_class(obj, a_class):
    """ Function that checks if an object is an instance
    of a specified class
    """
    return type(obj) is a_class
