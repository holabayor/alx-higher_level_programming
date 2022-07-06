#!/usr/bin/python3
""" Search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line to a text file after each
    line containing a specific string
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = ""
        for line in f.readlines():
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
