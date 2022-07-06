#!/usr/bin/python3
"""Read file module
"""


def read_file(filename=""):
    """
    This function reads a file and prints its content
    to the stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
