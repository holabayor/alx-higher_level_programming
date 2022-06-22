#!/usr/bin/python3


"""Define a class sqaure"""


class Square:
    """Definition of a class square"""

    def __init__(self, size=0, position=(0,0)):
        """Initializes a new square

        Args:
            size (int): The size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Attribute to retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """The property setter of the square to set its size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        area = self.__size * self.__size
        return area


    @property
    def position(self):
        """ Attribute to retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """The property setter of the square to set its position"""
        if not isinstance(value[0] or value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                [print("", end="") for j in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[1])]
                [print("#", end="") for k in range(self.__size)]
                print("")
