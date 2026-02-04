#!/usr/bin/python3
"""Module that defines mixins and a Dragon class.

This module provides SwimMixin and FlyMixin classes that add
swimming and flying capabilities, and a Dragon class that uses both.
"""


class SwimMixin:
    """Mixin class that provides swimming capability.

    This mixin adds the ability to swim to any class that inherits it.
    """

    @staticmethod
    def swim():
        """Make the creature swim.

        Prints a message indicating the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability.

    This mixin adds the ability to fly to any class that inherits it.
    """

    @staticmethod
    def fly():
        """Make the creature fly.

        Prints a message indicating the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying capabilities.

    This class combines SwimMixin and FlyMixin to create a dragon
    that can both swim and fly, and also roar.
    """

    @staticmethod
    def roar():
        """Make the dragon roar.

        Prints a message indicating the dragon is roaring.
        """
        print("The dragon roars")
