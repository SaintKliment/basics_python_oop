class Vector:
    def __init__(self, name, x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y 
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return (F"Hello, {self.name}!")
    


v = Vector('Vanya')
print(str(v))