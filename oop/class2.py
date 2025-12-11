#!/usr/bin/python3

"""Creating objects"""

class Dog:
    def __init__(self, name, breed, age, color):
        """Instance/objects attributes"""
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    """Object/Instance methods"""
    def bark(self):
        print(f"{self.breed} breeds bark the loudest.")

    def run(self):
       print("{} breeds aged {} years old are the fastest.".format(self.breed, self.age))

    def aesthetic(self):
        print(f"{self.breed} breeds with {self.color} color are very attractive")
    
    def hunting(self):
        print("{} breeds are very active in hunting, please consider having one.".format(self.breed))

    def naming(self):
        print(f"Dogs with {self.name} are very aggresive, please avoid them!")
 

# Taking input from the object from the user's input
dog1 = input("Whats the name of your dog?: ")
dog2 = input("Whats the breed of your dog?: ")
dog3 = int(input("How old is your dog?: "))
dog4 = input("Whats the color of your dog?: ")

# creating the object from the user input
dog = Dog(dog1, dog2, dog3, dog4)
# Accessing the attributes of the object
print("Name: ", dog.name)
print("Breed: ", dog.breed)
print("Age: ", dog.age)
print("Color: ", dog.color)

# Accessing the object methoddsa
dog.bark()
dog.run()
dog.aesthetic()
dog.hunting()
dog.naming()
