#!/usr/bin/python3


import math


class MagicClass:
    """Represents a class with magic methods to calculate the
    area and circumference of a circle."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass instance with a given radius.
        Args:
        radius (int, float): The radius of the circle. Defaults to 0.
        Raises:
        TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle.
        Returns:
        float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculates the circumference of the circle.
        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
