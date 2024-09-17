class Battery:
    
    def __init__(self, size):
        self.battery_size = size
        self.charge_leve = 0
        
    def charge_battery_full(self):
        print("charging the battery for you....")
        self.charge_level = 100
        
    def get_charge_level(self):
        return self.charge_level