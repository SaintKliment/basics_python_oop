# Single Inheritance
class Animal: 
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Wooh!')

# Multiple Inheritance
class Swim:
    def swim(self):
        print('Swimming...')

class Duck(Animal, Swim):
    def make_sound(self):
        print('Quack')

# Multi-level Inheritance
class Mammal(Animal):
    def feed_milk(self):
        print('Feeding milk...')

class Cat(Mammal):
    def make_sound(self):
        print('Wooh!')