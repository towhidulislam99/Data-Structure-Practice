from car import Car
from electric_car import ElectricCar

# car = Car('Honda', 'Accord', '2015')


# print(car.get_fuel_level())  

# car.fill_tank()

# print(car) 

my_electric_car = ElectricCar('Tesla', 'Model S', '2022')
print(my_electric_car)

# Print the initial charge level (should be 0)
print(f"Initial charge level: {my_electric_car.get_charge_level()}%")

# Charge the battery to full
print(my_electric_car.charge_battery_full())
