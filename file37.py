class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"Person('{self.name}, {self.age}')"

p = Person('zhenya', 16)
print (str(p))
print (repr(p))