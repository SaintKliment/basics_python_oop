class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('Generic Animal Sound')
    
class Cat(Animal):
    def make_sound(self):
        print('Meow')

cat = Cat('Fluffy')
cat.make_sound()
