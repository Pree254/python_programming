#!/usr/bin/python3

"""Classes and Objects"""

class Car:
    def __init__(self, make, model, year):
        """instance/object attributes"""
        self.make = make
        self.model = model
        self.year = year

    """Instance/objects methods/behaviours/functions"""
    def race(self):
        print("{} are best for racing." .format(self.make))

    def hoot(self):
        print("Beep! beep!")

    def transporter(self):
        print(f"{self.make} are best suited for transportation.")

# Creating instance of a class(object)
car1 = Car("BMW", "X6", 2025)

# Accessing object attributes
print("Make: ", car1.make)
print("Model: ", car1.model)
print("Year: ", car1.year)

# Accessing object methods
car1.race()
car1.hoot()
car1.transporter()


