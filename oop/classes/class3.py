#!/usr/bin/python3

"""Classes and Objects"""

class Reptilias:
    def __init__(self, name, age, habitat, meal):
        """Instance attributes/instance(object) variables"""
        self.name = name
        self.age = age
        self.habitat = habitat
        self.meal = meal

        """ Instance/object methods"""
    def swim(self):
        print(f"{self.name} is very swift in {self.habitat}, please take care!")

    def predator(self):
        print("{} is an apex predator in {}, and its favourite meal is {}.".format(self.name, self.habitat, self.meal))

    def bask(self):
        print(f"{self.name} are poikilotherms and do bask on shores to radiate.")      

    def __str__(self):
        return f"My favourite reptile is {self.name} aged {self.age} years old. "


# User input to create an object
rept = input("What's the name of your reptile?: ")
aging = int(input("How old do you think thid reptile is?: "))
habit =input("What's the habitat of this reptile?: ")
meal = input("What's the favourite meal of this reptile?: ") 

# Creating the object
reptile = Reptilias(rept, aging, habit, meal)
              
# Accessing objects attributes
print("Name: ", reptile.name)
print("Age: ", reptile.age)
print("Habitat: ", reptile.habitat) 
print("meal: ", reptile.meal)

# Accessing objects methods
reptile.swim()
reptile.predator()
reptile.bask()

# Accesing object using string
print(reptile)
