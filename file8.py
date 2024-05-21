class SomeClass(object):
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print('удаляется обьект {} класса SomeClass'.format(self.name))

obj = SomeClass("John")
del obj