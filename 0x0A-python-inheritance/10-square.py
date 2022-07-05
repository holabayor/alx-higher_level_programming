#!/usr/bin/python3
"""
This module implements a square object
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square implementation
    """
    def __init__(self, size):
        """ Initilization

        Args:
            size (int) : size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area

        Returns:
            area of the square
        """
        return self.__size * self.__size
