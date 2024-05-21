class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print('Meow')

class Dog(Animal):
    def make_sound(self):
        print('Woof!')

def animal_sound(animal):
    animal.make_sound()

dog = Dog('Buddy')
car = Cat('Fluffy')

animal_sound(dog)
animal_sound(cat)