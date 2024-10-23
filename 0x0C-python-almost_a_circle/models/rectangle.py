#!/usr/bin/python3
""" this modules defines the Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """ rectangle inherits base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialises Rectangle attributes
        Args:
            width: width
            height: height
            x: x
            y: y
            id: id attribute from base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ return the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """
        args assigns args to each atribute in the order listed in attributes
        kwargs assigns based on key
        """
        if args:
            attribute = ["id", "_Rectangle__width", "_Rectangle__height",
                         "_Rectangle__x", "_Rectangle__y"]
            for i, arg in enumerate(args):
                if i < len(attribute):
                    setattr(self, attribute[i], arg)
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'width':
                self.__width = value
            elif key == 'height':
                self.__height = value
            elif key == 'x':
                self.__x = value
            elif key == 'y':
                self.__y = value

    def __str__(self):
        """prints out rectangle details"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height))

    def area(self):
        """ public mthod to compute area"""
        return self.__width * self.__height

    def display(self):
        """displays the size of the rectangle"""
        print("\n" * self.__y, end="")

        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
