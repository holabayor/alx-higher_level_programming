#!/usr/bin/python3
""" Class to JSON Module
"""


def class_to_json(obj):
    """
    This function writes an object file
    into a text file
    """
    return obj.__dict__
