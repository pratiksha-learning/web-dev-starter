# Objects are dictionaries

class Employee:
    def __init__(self):
        self.name = 'Pratiksha'
        self.age = '24'

e = Employee()
print(e.__class__)

# __dict__ will call internally __new__ and then __init__ and pass parameter to self
print(e.__dict__) 

# we can directly call objects parameters
print(e.name)