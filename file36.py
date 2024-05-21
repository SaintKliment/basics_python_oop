class SomeClass():
    def __init__(self, value):
        self.value = value
    
    def __sub__(self, number):
        return self.value - number
    
s = SomeClass(11)
print (s - 10)
