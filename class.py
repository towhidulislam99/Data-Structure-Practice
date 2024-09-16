class Person:
    def __init__(self, first_name, last_name, age, gender, address):  # Fixed 'addess' to 'address'
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_age(self):
        return self.age
        
    def get_gender(self):
        return self.gender  # Fixed 'self.gener' to 'self.gender'
        
    def get_address(self):
        return self.address
        
    def describe_user(self):
        print(f"First Name is: {self.first_name} and Last Name is: {self.last_name}, Age is: {self.age} and Gender: {self.gender}")

# Creating an instance of the Person class
user_data = Person("Towhidul", "Islam", 20, "Male", "Bagdha")

# Using describe_user method to display the user data
user_data.describe_user()
