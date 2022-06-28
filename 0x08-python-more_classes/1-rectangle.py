#!/usr/bin/python3
"""Module for the Rectangle class"""


class Rectangle:
    """Definition of a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the rectangles height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
