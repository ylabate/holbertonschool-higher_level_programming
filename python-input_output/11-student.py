#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = {}
        if attrs and type(attrs) is list:
            for key, item in self.__dict__.items():
                if key in attrs:
                    dict[key] = item
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json.copy()
