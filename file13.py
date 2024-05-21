class SomeClass():
    def __init__(self):
        self.__param = 42 # защищенный атрибут
        
obj = SomeClass()
# obj.__param # AttributeError: 'SomeClass' object has no attribute '__param'
obj._SomeClass__param # 42