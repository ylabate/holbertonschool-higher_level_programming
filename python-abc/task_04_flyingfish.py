#!/usr/bin/python3
"""Module for multiple inheritance demonstration with Fish, Bird, and
FlyingFish classes.

This module illustrates multiple inheritance in Python where a class
inherits from multiple parent classes. FlyingFish demonstrates method
overriding and method resolution order (MRO).
"""


class Fish:
    """A class representing a fish with swimming and habitat behaviors.

    This class provides basic behaviors for aquatic creatures.
    """

    @staticmethod
    def swim():
        """Display the fish's swimming behavior.

        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    @staticmethod
    def habitat():
        """Display the fish's habitat preference.

        Prints a message indicating where the fish lives.
        """
        print("The fish lives in water")


class Bird:
    """A class representing a bird with flying and habitat behaviors.

    This class provides basic behaviors for aerial creatures.
    """

    @staticmethod
    def fly():
        """Display the bird's flying behavior.

        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    @staticmethod
    def habitat():
        """Display the bird's habitat preference.

        Prints a message indicating where the bird lives.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish with Fish and Bird behaviors.

    This class demonstrates multiple inheritance by inheriting from Fish
    and Bird classes. It overrides methods from both parent classes to
    provide specific behaviors for a creature that swims and flies.
    """

    @staticmethod
    def fly():
        """Display the flying fish's flying behavior.

        Overrides Bird.fly to provide specific output for flying fish.
        Prints a message indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    @staticmethod
    def swim():
        """Display the flying fish's swimming behavior.

        Overrides Fish.swim to provide specific output for flying fish.
        Prints a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    @staticmethod
    def habitat():
        """Display the flying fish's habitat preference.

        Overrides habitat from parent classes to indicate that the flying
        fish lives in both water and sky environments.
        """
        print("The flying fish lives both in water and the sky!")
