#!/usr/bin/python3
"""Read file module
"""


def append_write(filename="", text=""):
    """
    This function writes to a file and create it if it
    doesn't already exist
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
