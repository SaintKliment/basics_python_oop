class Mammal():
    className = 'Mammal'

class Dog(Mammal):
    species = 'Canis lupus'
dog = Dog()
dog.className
print(dog.className)
print(dog.species)