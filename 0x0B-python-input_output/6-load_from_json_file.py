#!/usr/bin/python3
""" Module to creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    This function creates an object
    from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
