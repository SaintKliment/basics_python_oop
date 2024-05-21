class SomeClass():
    def __init__(self, value):
        self._value = value

    def getvalue(self): # получение значения атрибута
        return self._value
    
    def setvalue(self, value): # установка значения атрибута
        self._value = value

    def delvalue(self): # удаление атрибута
        del self._value

    value = property(getvalue, setvalue, delvalue, "Свойство value")

obj = SomeClass(42)
print(obj.value)
obj.value = 43