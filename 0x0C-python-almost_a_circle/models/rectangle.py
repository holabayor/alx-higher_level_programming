#!/usr/bin/python3
"""Rectangle object"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle object implementation
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name: str, value: int, not_zero=True) -> None:
        """Validates the input values
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not_zero:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @width.setter
    def x(self, value):
        self.validate('x', value, False)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @width.setter
    def y(self, value):
        self.validate('y', value, False)
        self.__y = value
