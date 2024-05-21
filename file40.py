class Car:
    color = "black" # Class attribute

    def __init__(self, make, model):
        self.make = make
        self.model = model

c1 = Car("Ford", "Mustang")
c2 = Car("Chevrolet", "Camaro")


print(c1.color)
print(c2.color)

c1.color = 'red'

print(c1.color)
print(c2.color)