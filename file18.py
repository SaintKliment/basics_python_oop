class Horse():
    isHorse = True

class Donkey():
    isDonkey = True

class Mule(Horse, Donkey):
    def __init__(self):
        a = 1
mule = Mule()
print (mule.isHorse) # True
print (mule.isDonkey) # True