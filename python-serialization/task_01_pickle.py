#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Is Student: " + self.is_student)
    
    def serialize(self, filename):
        pickle.dump(self, filename)
    
    @classmethod
    def deserialize(cls, filename):
        return pickle.load(filename)
