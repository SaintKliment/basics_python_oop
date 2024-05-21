class Car():
    num_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.num_cars += 1

    @classmethod
    def show_num_cars(cls):
        print("Number of cars: ", cls_num_cars)
    
    def show_car_info(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)

s = Car('ford', 'mustang', '2000')
print(s.show_car_info())