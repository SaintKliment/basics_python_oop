list = ['hello', 'world']
len(list) # 2
class Collection:
    def __init__(self, list):
        self.list = list
    def __len__(self):
        return len(self.list)

collection = Collection([1,2,3])
a = len(collection) # 3
print(a)