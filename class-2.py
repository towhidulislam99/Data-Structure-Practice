class Animal:
    
    def __init__(self, name, color, call):
        self.name = name
        self.color = color
        self.call = call
        
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_call(self):
        return self.call
    
    def display_value(self):
        print(f"Animal Name: {self.name} Color is: {self.color} and its call : {self.call}")
        

give = Animal("Dog", "Black", "Gew Gew")
give1 = Animal("Cat", "White", "Mew Mew")

print(give)
print(give1)
give.display_value()
give1.display_value()
        
    