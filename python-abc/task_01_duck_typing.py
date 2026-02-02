from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> str:
        pass

    @abstractmethod
    def perimeter(self) -> str:
        pass


class Circle(Shape):
    def __init__(self, radius):
        if type(radius) is int:
            self.__radius = radius
        else:
            raise TypeError("radius should be a integer")

    def area(self):
        return "Area: " + str((self.__radius ** 2) * pi)

    def perimeter(self):
        return "Perimeter: " + str(2 * pi * self.__radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width should be a integer")
        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height should be a integer")

    def area(self):
        return "Area: " + str(self.__width * self.__height)

    def perimeter(self):
        return "Perimeter: " + str(self.__width * 2 + self.__height * 2)


def shape_info(shape):
    try:
        print(shape.area())
        print(shape.perimeter())
    except TypeError:
        raise TypeError("shape should be a child of Shape")
