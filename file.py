class SomeClass(object):
    attr1 = 42

    def method1(self, x):
        return 2*x
obj = SomeClass()
print (obj.method1(10))
print (obj.attr1)