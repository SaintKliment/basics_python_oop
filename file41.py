class A:
    def method(self):
        print('A')

class B(A):
    pass

class C(A):
    def method(self):
        print('C')

class D(B, C):
    pass

d = D()
d.method()