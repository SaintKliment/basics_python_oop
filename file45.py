class Soda:
    def __init__(self, bonus):
        self.bonus = bonus

    def show_my_drink(self):
        if (self.bonus == 'ничего'):
            return ("Обычная газировка")
        else:
            return (f"Газировка и {self.bonus}")

s = Soda('ничего')
print(s.show_my_drink())