#!/usr/bin/python3
"""
This module implements a customised list object
"""


class MyList(list):
    """
    My ALX customised list
    """
    def print_sorted(self):
        """
        This method prints the a sorted list in ascending order
        """
        print(sorted(self))
