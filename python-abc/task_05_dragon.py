#!/usr/bin/python3
class SwimMixin:
    @staticmethod
    def swim():
        print("The creature swims!")


class FlyMixin:
    @staticmethod
    def fly():
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    @staticmethod
    def roar():
        print("The dragon roars")
