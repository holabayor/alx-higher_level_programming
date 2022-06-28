#!/usr/bin/python3
"""This is a LockedClass"""


class LockedClass:
    """This class prevents users from
        creating new instances attributes
    """
    __slots__ = ["first_name"]
