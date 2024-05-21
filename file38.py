class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


l = MyList([1, 2, 3])
print (len(l))