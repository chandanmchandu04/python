class car:
    total_car = 0
    
    def __init__(self, brand, model):
     self.brand = brand
     self.model = model
     car.total_car += 1

    def full_name(self):
       return f"{self.brand} {self.model}"
    
    def fuel_type(self):
       return "petrol or Diesel"
    
class ElectricCar(car):
   def __init__(self, brand, model, battery_size):
      super(). __init__(brand, model)
      self.battery_size = battery_size

def fuel_type(self):
       return "Electric charge"
    

my_tesla = ElectricCar("Tesla", "model s", "100KWh")
print(my_tesla.full_name())
print(my_tesla.fuel_type())

safari = car("tata", "safari")
print(safari.fuel_type())

my_car = car("mahindra", "Thar")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = car("tata", "safari")
print(my_new_car.model)
print(my_new_car.brand)
print(my_new_car.full_name())