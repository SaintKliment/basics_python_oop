class SomeClass():
    def __init__(self, znak):
        self.znak = znak
    
    def __str__(self):
        return (f"{self.znak}")

    def __neg__(self):
        return self.znak[::-1]

s = SomeClass('а роза упала на лапу азора')
print(str(s))
print(-s)