class SomeClass():
    def __init__(self, value):
        self.value = value
    def __mul__(self, number):
        return self.value*number

obj = SomeClass(12)
print(obj * 100)