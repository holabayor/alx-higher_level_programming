#!/usr/bin/python3
"""Reads and return a JSON object
"""
import json

def to_json_string(my_obj):
    """
    This function returns a JSON representation
    of an object
    """
    return json.dumps(my_obj)
