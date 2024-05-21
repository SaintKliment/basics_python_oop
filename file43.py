class LogginMixin:
    def log(self, message):
        print(message)

class MyList(list, LogginMixin):
    pass

l = MyList([1, 2, 3])
l.log('This is message')