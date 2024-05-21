class SomeClass():
    attr1 = 42

    def __getattribute__(self, attr):
        return attr.upper()

obj = SomeClass()
print (obj.attr1)
print (obj.attr2)