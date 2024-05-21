class Multiplier:
    def __call__(self, x, y):
        return x*y
multiple = Multiplier()
multiple(19, 19) # 361
 # то же самое
multiple.__call__(19, 19) # 361