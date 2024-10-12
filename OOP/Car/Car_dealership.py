from OOP.Car.Car import car


car1 = car("Mustang", 2024, "Black", True)
car2 = car("Logan", 2003, "Blue", True)
car3 = car("Focus", 2018, "Red", False)



print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()