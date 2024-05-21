class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimetr(self):
        return (self.width + self.height) * 2

    def width(self, value):
        if value <= 0:
            raise ValueError("Width  must be positive!")
        self.width = value

    def height(self, value):
        if value <= 0:
            raise ValueError('Height must be positive!')
        self.height = value
    
r = Rectangle(10, 5)
print(r.area)
print(r.perimetr)
r.width = 20
print(r.area)