#!/usr/bin/python3


"""Define a class rectangle"""


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
        """Getter method for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if not (self.__width or self.__height):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle"""
        if not (self.__width or self.__height):
            return ("")
        rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                rec.append("#")
            if (i < self.__height - 1):
                rec.append("\n")
        return "".join(rec)