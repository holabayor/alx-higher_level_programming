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
            width (int) : size
        """
        self.integer_validator("szie", size)
        self.__size = size

    def area(self):
        """ area

        Returns:
            area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """str

        Returns:
            string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
