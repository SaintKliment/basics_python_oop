class Soda:
    def __init__(self, ing = None):
        if isinstance(ing, str):
            self.ing = ing
        else:
            self.ing = None
    
    def show_my_drink(self):
        if self.ing:
            print(f"Газировка и {self.ing}")
        else:
            print("Обычная газировка")

s = Soda('dasda')
print(s.show_my_drink())