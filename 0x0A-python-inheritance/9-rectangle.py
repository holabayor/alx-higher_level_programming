#!/usr/bin/python3
"""
This module implements a rectangle object
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle implementation
    """
    def __init__(self, width, height):
        """ Initilization

        Args:
            width (int) : width
            height (int) : height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area

        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """str

        Returns:
            string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
