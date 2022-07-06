#!/usr/bin/python3
""" Module to write an Object into a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object file
    into a text file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
