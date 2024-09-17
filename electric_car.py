from car import Car

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
        self.battery_size = 70
        self.charge_level = 0
    
    def charge_battery_full(self):
        self.charge_level = 100
        
    def get_charge_level(self):
        return self.charge_level
        
        