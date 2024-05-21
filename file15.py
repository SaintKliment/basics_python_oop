class SomeClass():
    attr1 = 42

    def __getattr__(self, attr):
        return attr.upper()

obj = SomeClass()
print (obj.attr1) # 42 &nbsp; nbsp;
print (obj.attr2) # ATTR2