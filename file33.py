class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = 123456

    def display_info(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('ID:', self.__id)

person = Person('zhenya', 16)
person.display_info()
