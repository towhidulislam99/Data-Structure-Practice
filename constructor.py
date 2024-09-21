class Person:
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #Method
    def Introduction(self):
        return f"I am {self.name} and my age is: {self.age}"
    
# create a Object in Person Class
person1 = Person('Md Towhidul Islam', 26)
person2 = Person('Abdullah Talukder', 3)

#Call the Function
print(person1.Introduction())
print(person2.Introduction())