#Python class with constructor
class Car:
    category = 'Vehicle'

    def _init_(self,name):
        self.name = name

new_car = Car('Audi')
print(new_car.name)